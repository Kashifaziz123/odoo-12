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


models.load_models({
        model:  'optical.dr',
        fields: ['name'],
        loaded: function(self,dr){
            self.dr =dr;
            self.db.doctors = dr;
        },
    });

models.load_models({
        model:  'dr.prescription',
//        fields: ['id','name','dr','customer','checkup_date','test_type','prescription_type','state','od_sph_distance'],
        loaded: function(self,optical_orders){
            self.db.optical_all_orders = optical_orders;
            self.products = optical_orders;
            self.db.optical_order_by_id = {};
            optical_orders.forEach(function(order){
                self.db.optical_order_by_id[order.id] = order;
            });
        },
    })

models.load_models({
        model:  'res.partner',
        fields: ['name','customer_rank'],
//        domain: [['customer_rank','=','1']],
        loaded: function(self,customers){
            self.customers = customers;
        },
    });

models.load_models({
        model:  'eye.test.type',
        fields: ['name'],
        loaded: function(self,test_type){
            self.test_type = test_type;
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
        var self = this;
        this._super();
         var optometrist = [];
        var partner = [];
        var test_types=[];
        var od_sph_distances=[];

        for (var i in self.pos.dr){
            optometrist.push(self.pos.dr[i].name);

        }
         for (var i in self.pos.customers){
            partner.push(self.pos.customers[i].name);
        }
         for (var i in self.pos.test_type){
            test_types.push(self.pos.test_type[i].name);
        }
         for (var i in self.pos.products){
            od_sph_distances.push(self.pos.products[i].od_sph_distance);

        }
        var abc= [];
        for (var i=0;i<90;i++)
            abc.push(i);
         self.gui.show_popup('product_create',{
                'doctors':optometrist,
                'partners':partner,
                'test_type':test_types,
                'od_sph_distance':od_sph_distances,
                'abc':abc,
            });

        },


    });

    screens.define_action_button({
        'name': 'book_order',
        'widget': button_book_order
    });



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
        this.doctors = options.doctors;
        this.partners = options.partners;
        this.test_type = options.test_type;
        this.od_sph_distances = options.od_sph_distances;
        this.abc= options.abc;
        this.renderElement();

    },
    click_confirm: function(){
        var self = this;
        var order = this.pos.get_order();
        var doctor = this.$('.doctor').val();
        var partner = this.$('.partner').val();
        var test_type = this.$('.test_type').val();
        var age = this.$('.age').val();
        var checkup_date = this.$('.checkup_date').val();
        var prescription_type = this.$('.prescription_type').val();
        var eyes_charges = this.$('.eye_charges').val();
        var eyes_history = this.$('.eyes_history').val();
        var ocular_history  = this.$('.ocular_history').val();
        var consultation_reason = this.$('.consultation_reason').val();
        var diagnosis_client = this.$('.diagnosis_client').val();
        var notes_laboratory = this.$('.notes_laboratory').val();
        var optometrist_observation = this.$('.optometrist_observation').val();
        var od_sph_distance = this.$('.od_sph_distance').val();
        var od_cyl_distance = this.$('.od_cyl_distance').val();
        var od_axis_distance = this.$('.od_axis_distance').val();
        var od_add_distance = this.$('.od_add_distance').val();
        var od_prism_distance = this.$('.od_prism_distance').val();
        var od_base_distance = this.$('.od_base_distance').val();
        var os_sph_distance = this.$('.os_sph_distance').val();
        var os_cyl_distance = this.$('.os_cyl_distance').val();
        var os_ax_distance = this.$('.os_ax_distance').val();
        var os_add_distance  = this.$('.os_add_distance').val();
        var os_prism_distance = this.$('.os_prism_distance').val();
        var os_base_distance = this.$('.os_base_distance').val();
        var od_sph_near = this.$('.od_sph_near').val();
        var od_cyl_near = this.$('.od_cyl_near').val();
        var od_ax_near = this.$('.od_ax_near').val();
        var od_add_near = this.$('.od_add_near').val();
        var od_prism_near  = this.$('.od_prism_near').val();
        var od_base_near  = this.$('.od_base_near').val();
        var  os_sph_near = this.$('.os_sph_near').val();
        var os_cyl_near = this.$('.os_cyl_near').val();
        var os_ax_near = this.$('.os_ax_near').val();
        var os_add_near = this.$('.os_add_near').val();
        var os_prism_near = this.$('.os_prism_near').val();
        var os_base_near = this.$('.os_base_near').val();



        var today = new Date().toJSON().slice(0,10);
        if( !checkup_date) {
              this.gui.show_popup('error',{
                    'title': _t('Checkup date is empty'),
                    'body':  _t('You need to select a Checkup date'),
                cancel: function () {

                 var optometrist = [];
        var partner = [];
        var test_types=[];
        var od_sph_distances=[];

        for (var i in self.pos.dr){
            optometrist.push(self.pos.dr[i].name);

        }
         for (var i in self.pos.customers){
            partner.push(self.pos.customers[i].name);
        }
         for (var i in self.pos.test_type){
            test_types.push(self.pos.test_type[i].name);
        }


                    this.gui.show_popup('product_create',{
                'doctors':optometrist,
                'partners':partner,
                'test_type':test_types,

            });
                },

                });
        }
        else {
          this.gui.show_popup('confirm',{
                'title': _t('Create a Prescription ?'),
                'body': _t('Are You Sure You Want a Create a Prescription'),
                confirm: function(){
                  var product_vals = {
                        'doctor':doctor,
                        'partner':partner,
                        'checkup_date':checkup_date,
                        'test_type':test_type,
                        'prescription_type':prescription_type,
                        'eyes_charges':eyes_charges,
                        'eyes_history':eyes_history,
                        'ocular_history':ocular_history,
                        'consultation_reason':consultation_reason,
                        'diagnosis_client':diagnosis_client,
                        'notes_laboratory':notes_laboratory,
                        'optometrist_observation':optometrist_observation,
                        'od_sph_distance':od_sph_distance,
                        'od_cyl_distance':od_cyl_distance,
                        'od_axis_distance':od_axis_distance,
                        'od_add_distance':od_add_distance,
                        'od_prism_distance':od_prism_distance,
                        'od_base_distance':od_base_distance,
                        'os_sph_distance':os_sph_distance,
                        'os_cyl_distance':os_cyl_distance,
                        'os_ax_distance':os_ax_distance,
                        'os_add_distance':os_add_distance,
                        'os_prism_distance':os_prism_distance,
                        'os_base_distance':os_base_distance,
                        'od_sph_near':od_sph_near,
                        'od_cyl_near':od_cyl_near,
                        'od_ax_near':od_ax_near,
                        'od_add_near':od_add_near,
                        'od_prism_near':od_prism_near,
                        'od_base_near':od_base_near,
                        'os_sph_near':os_sph_near,
                        'os_cyl_near':os_cyl_near,
                        'os_ax_near':os_ax_near,
                        'os_add_near':os_add_near,
                        'os_prism_near':os_prism_near,
                        'os_base_near':os_base_near,
                 };
                  rpc.query({
                    model: 'dr.prescription',
                    method: 'create_product_pos',
                    args: [product_vals],
                }).then(function (products){
                        self.pos.db.add_optical_orders(products)
                        $('.optical_prescription').text(products.name);
                        order.set_optical_reference(products);
                        console.log(products)
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