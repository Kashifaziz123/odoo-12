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
        },
    });

models.load_models({
        model:  'dr.prescription',
        fields: ['name','dr','customer','checkup_date','test_type','prescription_type','state','od_sph_distance'],
        loaded: function(self,products){
            self.products = products;
        },
    })

models.load_models({
        model:  'res.partner',
        fields: ['name','customer_rank'],
        domain: [['customer_rank','=','1']],
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
            this.gui.show_screen('product-list');
            var self = this;
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
         self.gui.show_popup('product_create',{
                'doctors':optometrist,
                'partners':partner,
                'test_type':test_types,
                'od_sph_distance':od_sph_distances
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
        this.renderElement();

    },
    click_confirm: function(){
        var self = this;
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
                    'title': _t('Error'),
                    'body':  _t('Required CheckUP Date'),
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
            this._super();
            this.renderElement();
            this.$('.back').click(function(){
                self.gui.show_screen('products');
            });

            var products = []
            for (var i=0;i < this.pos.products.length ;i++){
                      products.push(this.pos.products[i]);
            }

            self.products = products;
            this.render_list(products);
            this.$('.products-list-contents').delegate('.productlines','click',function(event){
                self.line_select(event,$(this.parentElement.parentElement),parseInt($(this.parentElement.parentElement).data('id')))
            });


            var search_timeout = null;

            if(this.pos.config.iface_vkeyboard && this.chrome.widget.keyboard){
                this.chrome.widget.keyboard.connect(this.$('.searchbox input'));
            }

            this.$('.searchbox input').on('keyup',function(event){
                clearTimeout(search_timeout);
                var query = this.value;
                search_timeout = setTimeout(function(){
                    self.perform_search(query,event.which === 13);
                },70);
            });

            this.$('.searchbox .search-clear').click(function(){
                self.clear_search();
            });
    },

    perform_search: function(query){
            var products;
            if(query){
               products = this.search_products(query);
                this.render_list(products);
            }else{
                products = this.pos.products;
                this.render_list(products);
    }
    },

    line_select: function(event,$line,id){

    },

    render_list: function(products){
            var length = products.length
            var contents = this.$el[0].querySelector('.products-list-contents');
            contents.innerHTML = "";
            for(var i = 0, len = Math.min(products.length); i < len; i++){
                var product    = products[i];
                var product_line_html = QWeb.render('ProductsLine',{widget: this, product:products[i]});
                var product_line = document.createElement('tbody');
                product_line.innerHTML = product_line_html;
                product_line = product_line.childNodes[1];
                contents.appendChild(product_line);
            }
    },

    search_products: function(query){
            try {
                var re = RegExp(query);
            }catch(e){
                return [];
            }
            var results = [];
            for (var product_id in this.pos.products){
                var r = re.exec(this.pos.products[product_id]['name']);
                var g = re.exec(this.pos.products[product_id]['dr']);
                if(r || g){
                results.push(this.pos.products[product_id]);
                }
            }
            return results;

        },









});

gui.define_screen({name:'product-list',widget:ProductWidget});









});