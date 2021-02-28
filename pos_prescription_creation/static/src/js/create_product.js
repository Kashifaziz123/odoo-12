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
//    },{
//        model:  'product.product',
//        loaded: function(self,products){
//            self.db.product_product = products;
//        },
    },{
// =====================================
//  To select all optical attributes ids
// =====================================
        model:  'product.attribute',
        fields: ['id','name'],
//        domain: [['name','in',['Type Of Focus', 'Material', 'Treatment', 'Photochromic', 'Filter', 'High Index', 'Carving',
//            'Special Works', 'Type Scope']]],
        domain: [['name','in',['Type Of Focus', 'Material', 'Treatment']]],
        loaded: function(self,attributes){
            self.db.optical_product_attributes_ids = [];
            for (var i=0;i< attributes.length;i++)
                self.db.optical_product_attributes_ids.push(attributes[i].id);
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

    models.load_models({
// =============================================
//  To select all products with optical variants
// =============================================
        model:  'product.template',
        fields: ['id','name', 'attribute_line_ids','product_variant_count','product_variant_ids'],
//        domain: [['product_variant_count', '=', 81]],
        loaded: function(self,product_templates){
            self.db.optical_glasses = [];
            self.db.optical_glasses_by_id = {};
            product_templates.forEach(function(product_template){
                self.db.attribute_line_ids = [];
                product_template.attribute_line_ids.forEach(function(attribute_line){
                    self.db.attribute_line_ids.push(self.db.product_attributes_lines_by_id[attribute_line].attribute_id[0]);
                })
                if (self.db.attribute_line_ids.length)
                    if (self.db.attribute_line_ids.every(function(id){return self.db.optical_product_attributes_ids.includes(id);})){
                        self.db.optical_glasses.push(product_template);
                        self.db.optical_glasses_by_id[product_template.id] = product_template;
                    }
            })
        },
    });


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
            if (vals["blue_light_filter"] == undefined)
                vals["blue_light_filter"] = 'No filter';
            else
                vals["blue_light_filter"] = 'BLF';
            if (vals["types_of_focus"] == undefined)
                vals["types_of_focus"] = 'No type';
            if (vals["high_index"] == undefined)
                vals["high_index"] = 'No index';
            if (vals["material"] == undefined)
                vals["material"] = 'No material';
            if (vals["carving"] == undefined)
                vals["carving"] = 'No carving';
            if (vals["special_works"] == undefined)
                vals["special_works"] = 'No special works';
            if (vals["treatment"] == undefined)
                vals["treatment"] = 'No treatment';
            if (vals["PhotoChromic"] == undefined)
                vals["PhotoChromic"] = 'No photochromic';
            if (vals["Type_Scope"] == undefined)
                vals["Type_Scope"] = 'No type scope';

            id = $('option:selected', $('[name=glasses]')).data('id');
            self.pos.db.optical_glasses_by_id[id].product_variant_ids.forEach(function(product_template){
                if (self.pos.db.product_by_id[product_template].display_name.includes(vals["types_of_focus"]) &&
                    self.pos.db.product_by_id[product_template].display_name.includes(vals["material"]) &&
                    self.pos.db.product_by_id[product_template].display_name.includes(vals["treatment"]))
                        order.add_product(self.pos.db.product_by_id[product_template])
            })
            self.gui.close_popup();
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