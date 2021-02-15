odoo.define('pos_product_creation',function(require) {

var gui = require('point_of_sale.gui');
var chrome = require('point_of_sale.chrome');
var PopupWidget = require('point_of_sale.popups');
var screens = require('point_of_sale.screens');
var popups = require('point_of_sale.popups');
var core = require('web.core');
var models = require('point_of_sale.models');
var rpc = require('web.rpc');
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
        model:  'res.partner',
        fields: ['name'],
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


 var button_book_order = screens.ActionButtonWidget.extend({
        template: 'button_book_order',
        button_click: function () {
        var self = this;
        this._super();
         var optometrist = [];
        var partner = [];
        var test_types=[];

        for (var i in self.pos.dr){
            optometrist.push(self.pos.dr[i].name);

        }
         for (var i in self.pos.customers){
            partner.push(self.pos.customers[i].name);
        }
         for (var i in self.pos.test_type){
            test_types.push(self.pos.test_type[i].name);
        }
         self.gui.show_popup('product_create',{
                'doctors':optometrist,
                'partners':partner,
                'test_type':test_types
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
        var os_axis_distance = this.$('.os_axis_distance').val();
        var os_add_distance  = this.$('.os_add_distance').val();
        var os_prism_distance = this.$('.os_prism_distance').val();
        var os_base_distance = this.$('.os_base_distance').val();
         var od_sph_near = this.$('.od_sph_near').val();
        var od_cyl_near = this.$('.od_cyl_near').val();
        var od_axis_near = this.$('.od_axis_near').val();
        var od_add_near = this.$('.od_add_near').val();
        var od_prism_near  = this.$('.od_prism_near').val();
        var od_base_near  = this.$('.od_base_near').val();
        var  os_sph_near = this.$('.os_sph_near').val();
        var os_cyl_near = this.$('.os_cyl_near').val();
        var os_axis_near = this.$('.os_axis_near').val();
        var os_add_near = this.$('.os_add_near').val();
        var os_prism_near = this.$('.os_prism_near').val();
        var os_base_near = this.$('.os_base_near').val();



        var today = new Date().toJSON().slice(0,10);
        if(!doctor || !partner) {
            alert("Please Select The Optometrist OR Partner")
        }
        else if(!checkup_date) {
            alert("Please Select The Prescription Date")
        }
        else {
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
                'od_axis_distance':od_axis_distance,
                'os_add_distance':os_add_distance,
                'os_prism_distance':os_prism_distance
                '':
                 '':
                '':
                '':
                '':
                 '':
                '':
                '':
                '':

            };
            rpc.query({
                    model: 'dr.prescription',
                    method: 'create_product_pos',
                    args: [product_vals],
                }).then(function (products){
                         console.log(products)

                });
            this.gui.close_popup();
        }

        this.gui.close_popup();

    },

    click_cancel: function(){
        this.gui.close_popup();
        if (this.options.cancel) {
            this.options.cancel.call(this);
        }
    },

});
gui.define_popup({name:'product_create', widget: ProductCreationWidget});

});