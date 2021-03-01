odoo.define('pos_prescription_creation',function(require) {

    var gui = require('point_of_sale.gui');
    var chrome = require('point_of_sale.chrome');
    var PopupWidget = require('point_of_sale.popups');
    var screens = require('point_of_sale.screens');
    var popups = require('point_of_sale.popups');
    var core = require('web.core');
    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');
    var utils = require('web.utils');
    var QWeb = core.qweb;
    var _t = core._t;

    models.load_models([{
        model:  'optical.dr',
        fields: ['name'],
        loaded: function(self,dr){
            self.dr =dr;
            self.db.doctors = dr;
        },
    },{
        model:  'dr.prescription',
        loaded: function(self,optical_orders){
            self.db.optical_all_orders = optical_orders;
//            self.products = optical_orders;
            self.db.optical_order_by_id = {};
            optical_orders.forEach(function(order){
                self.db.optical_order_by_id[order.id] = order;
            });
        },
    },{
        model:  'res.partner',
        fields: ['name','customer_rank'],
//        domain: [['customer_rank','=','1']],
        loaded: function(self,customers){
            self.customers = customers;
        },
    },{
        model:  'eye.test.type',
        fields: ['name'],
        loaded: function(self,test_type){
            self.test_type = test_type;
        },
    },{
// =====================================
//  To select all optical attributes ids
// =====================================
        model:  'product.attribute',
        loaded: function(self,attributes){
            self.db.optical_product_attributes_by_id = {};
            self.db.optical_product_attributes = attributes;
            for (var i=0;i< attributes.length;i++)
                self.db.optical_product_attributes_by_id[attributes[i].id] = attributes[i];
        },
    },{
// ========================================
//  To select all template attributes lines
// ========================================
        model:  'product.template.attribute.line',
//        fields: ['id','attribute_id'],
        loaded: function(self,attributes){
            self.db.product_attributes_lines_by_id = {};
            attributes.forEach(function(attribute){
                self.db.product_attributes_lines_by_id[attribute.id] = attribute;
            });
        },
    }]);

    models.load_models([{
// =============================================
//  To select all products with optical variants
// =============================================
        model:  'product.template',
        fields: ['id','name', 'attribute_line_ids','product_variant_count','product_variant_ids'],
        loaded: function(self,product_templates){
            self.db.optical_glasses = [];
            self.db.optical_glasses_by_id = {};
            self.db.optical_glasses = product_templates.filter(function(el){return el.product_variant_count > 1});
            self.db.optical_glasses.forEach(function(optical_glass){
                self.db.optical_glasses_by_id[optical_glass.id] = optical_glass;
            });
        },
    },{
        model:  'product.attribute.value',
        loaded: function(self,attributes){
            self.db.optical_product_attribute_values_by_id = {};
            self.db.optical_product_attribute_values= attributes;
            attributes.forEach(function(attribute){
                self.db.optical_product_attribute_values_by_id[attribute.id] = attribute;
            });
            self.db.optical_product_attributes_for_xml = [];
            i = 0;
            self.db.optical_product_attributes.forEach(function(attribute){
                self.db.optical_product_attributes_for_xml[i] = {};
                self.db.optical_product_attributes_for_xml[i].name = attribute.name;
                self.db.optical_product_attributes_for_xml[i].attributes = [];
                attribute.value_ids.forEach(function(attribute_value_id){
                    self.db.optical_product_attributes_for_xml[i].attributes.push(self.db.optical_product_attribute_values_by_id[attribute_value_id].name);
                })
                i++;
            });
        },
    }]);

    var PrescriptionButton = screens.ActionButtonWidget.extend({
        template: 'PrescriptionButton',
        button_click: function(){
            this.gui.show_screen('product-list',this.pos.db.optical_all_orders);
        }
    });

    screens.define_action_button({
        'name': 'PrescriptionButton',
        'widget':PrescriptionButton,
    });

    var button_book_order = screens.ActionButtonWidget.extend({
        template: 'button_book_order',
        button_click: function () {
            this._super();
            this.gui.show_popup('product_create');
        },
    });

    screens.define_action_button({
        'name': 'book_order',
        'widget': button_book_order
    });

    var SelectGlassesButton = screens.ActionButtonWidget.extend({
        template: 'SelectGlassesButton',
        button_click: function () {
            this._super();
            this.gui.show_popup('order_create');
        },
    });

    screens.define_action_button({
        'name': 'SelectGlassesButton',
        'widget': SelectGlassesButton
    });

    var OrderCreationWidget = PopupWidget.extend({
        template: 'OrderCreationWidget',
        events: {
        'click .button.cancel':  'click_cancel',
        'click .button.confirm': 'click_confirm',
    },
        show: function(options){
            options = options || {};
            this._super(options);
            self = this;
            ceil = Math.ceil(self.pos.db.optical_product_attributes_for_xml.length / 2);
            this.variants1 = self.pos.db.optical_product_attributes_for_xml.slice(0, ceil);
            this.variants2 = self.pos.db.optical_product_attributes_for_xml.slice(ceil);
            this.glasses = self.pos.db.optical_glasses;
            if (this.pos.get_order().attributes.client)
                this.customer = this.pos.get_order().attributes.client.name;
            else
                this.customer = false;
            if (this.pos.get_order().optical_reference != undefined)
                this.optical_reference = this.pos.get_order().optical_reference.name;
            else
                this.optical_reference = false;
            if (!this.customer || !this.optical_reference){
                this.gui.show_popup('error',{
                    'title': _t('No Customer or Prescription found'),
                    'body':  _t('You need to select Customer & Prescription to continue'),
                });
            }
            else
                this.renderElement();
        },
        click_confirm: function(){
            var self = this;
            var order = this.pos.get_order();
            var vals = $("#order_form").serializeObject();
            id = $('option:selected', $('#glasses')).data('id');
            var found = false;

            variants = []
            self.pos.db.optical_glasses_by_id[id].attribute_line_ids.forEach(function(attribute_line_id){
                variants.push(self.pos.db.product_attributes_lines_by_id[attribute_line_id].display_name);
            })
            self.pos.db.optical_glasses_by_id[id].product_variant_ids.forEach(function(product_template){
                if (variants.every(function(variant){return self.pos.db.product_by_id[product_template].display_name.includes(vals[variant])})){
                    order.add_product(self.pos.db.product_by_id[product_template])
                    found = true;
                }
            })
            self.gui.close_popup();
            if (!found)
                this.gui.show_popup('error',{
                    'title': _t('No variant found'),
                    'body':  _t('The glasses selected have no variant base on selected attributes'),
                });
        },
        click_cancel: function(){
            this.gui.close_popup();
            if (this.options.cancel) {
                this.options.cancel.call(this);
            }
        },
    });
    gui.define_popup({name:'order_create', widget: OrderCreationWidget});



var ProductCreationWidget = PopupWidget.extend({
    template: 'ProductCreationWidget',
    init: function(parent, args) {
        this._super(parent, args);
        this.options = {};
        this.doctors = [];
        this.partners = [];
        this.test_type=[];
        this.od_sph_distances=[];
    },
    events: {
        'click .button.cancel':  'click_cancel',
        'click .button.confirm': 'click_confirm',
    },
    show: function(options){
        options = options || {};
        this._super(options);
        this.doctors = this.pos.dr;
        this.partners = this.pos.customers;
        this.test_type = this.pos.test_type;
        if (this.pos.get_order().attributes.client)
            this.customer = this.pos.get_order().attributes.client.id;
        else
            this.customer = false;
        var abc= [];
        for (var i=0;i<90;i++)
            abc.push(i);
        this.abc= abc;
        this.renderElement();

    },
    click_confirm: function(){
        var self = this;
        var order = this.pos.get_order();
        var vals = $("#prescription_form").serializeObject();
        vals["dr"] = $('option:selected', $('[name=dr]')).data('id');
        vals["customer"] = $('option:selected', $('[name=customer]')).data('id');
        vals["test_type"] = $('option:selected', $('[name=test_type]')).data('id');
        if (vals["dual_pd"] !== "on")
            vals["dual_pd"] = "off";
        vals = JSON.stringify(vals);
        var checkup_date = $('[name=checkup_date]').val();
        var today = new Date().toJSON().slice(0,10);
        if( !checkup_date) {
              this.gui.show_popup('error',{
                'title': _t('Checkup date is empty'),
                'body':  _t('You need to select a Checkup date'),
                cancel: function () {
                    this.gui.show_popup('product_create');
                },
              });
        }
        else {
            this.gui.show_popup('confirm',{
                'title': _t('Create a Prescription ?'),
                'body': _t('Are You Sure You Want a Create a Prescription'),
                    confirm: function(){
                        rpc.query({
                            model: 'dr.prescription',
                            method: 'create_product_pos',
                            args: [vals],
                        }).then(function (products){
                            self.pos.db.add_optical_orders(products)
                            $('.optical_prescription').text(products.name);
                            order.set_optical_reference(products);
                            order.set_client(self.pos.db.partner_by_id[$('option:selected', $('[name=customer]')).data('id')]);
                        });
                    },
            });
        };
    },
    click_cancel: function(){
        this.gui.close_popup();
        if (this.options.cancel) {
            this.options.cancel.call(this);
        }
    },
});
gui.define_popup({name:'product_create', widget: ProductCreationWidget});


var ProductWidget = screens.ScreenWidget.extend({
    template: 'Product-ListWidget-Custom',
    init: function(parent, options){
        this._super(parent, options);
    },
    show: function(){
            var self = this;
            var optical_orders = [];
            this._super();
            this.renderElement();
            this.$('.back').click(function(){
                self.gui.show_screen('products');
            });
            var order = this.pos.get_order();
            optical_order_ids = order.get_screen_data('params')
            if (optical_order_ids)
                for (var i=0; i < optical_order_ids.length; i++)
                    optical_orders.push(self.pos.db.optical_order_by_id[optical_order_ids[i].id])
            else
                var optical_orders = self.pos.db.optical_all_orders
            this.render_list(optical_orders, undefined, undefined);
            var search_timeout = null;
//            if(this.pos.config.iface_vkeyboard && this.chrome.widget.keyboard){
//                this.chrome.widget.keyboard.connect(this.$('.searchbox input'));
//            }
            this.$('.products-list-contents').on('click', '.productlines', function(event){
                self.line_select(event,$(this),parseInt($(this).data('id')));
            });
            this.$('.searchbox_date').keyup(function() {
                self.render_list(optical_orders, this.childNodes[1].value, undefined);
            });
            this.$('.searchbox_client').keyup(function() {
                self.render_list(optical_orders, undefined, this.childNodes[1].value);
            });
            this.$('.searchbox .search-clear').click(function(){
                self.clear_search();
            });
    },
    line_select: function(event,$line,id){
        var self = this;
		optical_order =  self.pos.db.optical_order_by_id[id]
    	var contents = this.$('.optical_order-details-content');
    	if (parseInt($('.prescription_receipt_details').data('id')) !== id){
        	contents.empty();
    		contents.append($(QWeb.render('PrescriptionShowTable',{widget:this, optical_order:optical_order})));
    	}
    	else
        	contents.empty();
    },
    render_list: function(optical_orders, date_value, client_value){
            var self = this
            var length = optical_orders.length
            var contents = this.$el[0].querySelector('.products-list-contents');
            contents.innerHTML = "";
            if (client_value)
                optical_orders = optical_orders.filter(function(el){return el.customer[1].toLowerCase().includes(client_value.toLowerCase())})
            if (date_value)
                optical_orders = optical_orders.filter(function(el){return el.checkup_date.toLowerCase().includes(date_value.toLowerCase())})
            len = Math.min(optical_orders.length)-1;
            for(var i = len ; i >= 0; i--){
                var optical_order = optical_orders[i];
                var optical_orders_line_html = QWeb.render('ProductsLine',{widget: this, product:optical_order});
                var optical_orders_line = document.createElement('tbody');
                optical_orders_line.innerHTML = optical_orders_line_html;
                optical_orders_line = optical_orders_line.childNodes[1];
                contents.appendChild(optical_orders_line);
            }
            this.$('.pos_optical_copy').click(function(event) {
                var order = self.pos.get_order();
                optical_order = self.pos.db.optical_order_by_id[parseInt($(this).data('orderId'))];
                $('.optical_prescription').text(optical_order.name);
                order.set_optical_reference(optical_order);
                self.gui.back();
            });
            this.$('.pos_optical_print').click(function(event) {
                self.gui.show_screen('PrescriptionReceipt',parseInt($(this).data('orderId')));
            });
    },
});
gui.define_screen({name:'product-list',widget:ProductWidget});

screens.ClientListScreenWidget.include({
    events: {
            'click .prescription_count_btn': 'prescription_count_btn',
	},
    display_client_details: function(visibility,partner,clickpos){
        var self = this;
        var searchbox = this.$('.searchbox input');
        var contents = this.$('.client-details-contents');
        var parent   = this.$('.client-list').parent();
        var scroll   = parent.scrollTop();
        var height   = contents.height();

        contents.off('click','.button.edit');
        contents.off('click','.button.save');
        contents.off('click','.button.undo');
        contents.on('click','.button.edit',function(){ self.edit_client_details(partner); });
        contents.on('click','.button.save',function(){ self.save_client_details(partner); });
        contents.on('click','.button.undo',function(){ self.undo_client_details(partner); });
        this.editing_client = false;
        this.uploaded_picture = null;
        count = 0
        if (partner)
            count = self.pos.db.optical_all_orders.filter(function(el){return el.customer[0] === partner.id}).length
        if(visibility === 'show'){
            contents.empty();
            contents.append($(QWeb.render('ClientDetails',{widget:this,partner:partner,prescription_count:count})));

            var new_height   = contents.height();

            if(!this.details_visible){
                // resize client list to take into account client details
                parent.height('-=' + new_height);

                if(clickpos < scroll + new_height + 20 ){
                    parent.scrollTop( clickpos - 20 );
                }else{
                    parent.scrollTop(parent.scrollTop() + new_height);
                }
            }else{
                parent.scrollTop(parent.scrollTop() - height + new_height);
            }

            this.details_visible = true;
            this.toggle_save_button();
        } else if (visibility === 'edit') {
            // Connect the keyboard to the edited field
            if (this.pos.config.iface_vkeyboard && this.chrome.widget.keyboard) {
                contents.off('click', '.detail');
                searchbox.off('click');
                contents.on('click', '.detail', function(ev){
                    self.chrome.widget.keyboard.connect(ev.target);
                    self.chrome.widget.keyboard.show();
                });
                searchbox.on('click', function() {
                    self.chrome.widget.keyboard.connect($(this));
                });
            }

            this.editing_client = true;
            contents.empty();
            contents.append($(QWeb.render('ClientDetailsEdit',{widget:this,partner:partner,prescription_count:count})));
            this.toggle_save_button();

            // Browsers attempt to scroll invisible input elements
            // into view (eg. when hidden behind keyboard). They don't
            // seem to take into account that some elements are not
            // scrollable.
            contents.find('input').blur(function() {
                setTimeout(function() {
                    self.$('.window').scrollTop(0);
                }, 0);
            });

            contents.find('.client-address-country').on('change', function (ev) {
                var $stateSelection = contents.find('.client-address-states');
                var value = this.value;
                $stateSelection.empty()
                $stateSelection.append($("<option/>", {
                    value: '',
                    text: 'None',
                }));
                self.pos.states.forEach(function (state) {
                    if (state.country_id[0] == value) {
                        $stateSelection.append($("<option/>", {
                            value: state.id,
                            text: state.name
                        }));
                    }
                });
            });

            contents.find('.image-uploader').on('change',function(event){
                self.load_image_file(event.target.files[0],function(res){
                    if (res) {
                        contents.find('.client-picture img, .client-picture .fa').remove();
                        contents.find('.client-picture').append("<img src='"+res+"'>");
                        contents.find('.detail.picture').remove();
                        self.uploaded_picture = res;
                    }
                });
            });
        } else if (visibility === 'hide') {
            contents.empty();
            parent.height('100%');
            if( height > scroll ){
                contents.css({height:height+'px'});
                contents.animate({height:0},400,function(){
                    contents.css({height:''});
                });
            }else{
                parent.scrollTop( parent.scrollTop() - height);
            }
            this.details_visible = false;
            this.toggle_save_button();
        }
    },
    prescription_count_btn: function(){
//        $(this)[0].$el[0].children[0].children[1].childNodes[1].childNodes[1].children[0].children[0].children[0].children[2].children[0].dataset['id']
        optical_orders = this.pos.db.optical_all_orders.filter(function(el){return el.customer[0] === $('.prescription_count_btn').data('id')})
        this.gui.show_screen('product-list', optical_orders);
    },
});

});