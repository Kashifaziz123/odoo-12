odoo.define('pos_prescription_creation.models', function(require){

    var ActionpadWidget = require("point_of_sale.screens").ActionpadWidget;  
	var PosBaseWidget = require('point_of_sale.BaseWidget');  
	var chrome = require('point_of_sale.chrome');
	var models = require('point_of_sale.models');
	var core = require('web.core');
	var gui = require('point_of_sale.gui');
	var screens = require('point_of_sale.screens');
	var _t = core._t;

    models.load_fields("pos.order", ['optical_reference']);
    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({

        init_from_JSON: function (json) {
            var res = _super_order.init_from_JSON.apply(this, arguments);
            if (json.optical_reference) {
                var optical_reference = this.pos.db.optical_order_by_id[json.optical_reference];
                if (optical_reference) {
                    this.set_optical_reference(optical_reference);
                }
            }
            return res;
        },

        export_as_JSON: function () {
            var json = _super_order.export_as_JSON.apply(this, arguments);
            if (this.optical_reference) {
                if (this.optical_reference[0])
                    json.optical_reference=this.optical_reference[0];
                else
                    json.optical_reference = this.optical_reference.id;
            }
            return json;
        },

        set_optical_reference: function (optical_reference) {
            this.optical_reference = optical_reference;
            this.trigger('change', this);
        },

    });

    models.PosModel = models.PosModel.extend({
        get_optical_reference: function() {
            var order = this.get_order();
            if (order.optical_reference) {
                optical_reference = this.db.optical_order_by_id[order.optical_reference.id]
                return optical_reference;
            }
            return null;
        },
    });

//    //Change Sales Person on order Click
//    chrome.OrderSelectorWidget.include({
//        order_click_handler: function(event,$el) {
//            this._super(event,$el);
//            var order = this.pos.get_order();
//            if (order!==null && order!==undefined && order.sales_person_id){
//                $(sales_person_button).text(" " + order.sales_person_id.name)
//            }
//            else{
//                $(sales_person_button).text(" Sales Person")
//            }
//        },
//
//        neworder_click_handler: function(event, $el) {
//            this._super(event, $el);
//            $(sales_person_button).text(" Sales Person")
//        },
//
//        deleteorder_click_handler: function(event,$el) {
//            this._super(event,$el);
//            var order = this.pos.get_order();
//            if (order!==null && order!==undefined && order.sales_person_id){
//                $(sales_person_button).text(" " + order.sales_person_id.name)
//            }
//            else{
//                $(sales_person_button).text(" Sales Person")
//            }
//        },
//    });

    //Change Sales Person on new order after payment done
	screens.PaymentScreenWidget.include({
        validate_order: function(force_validation){
            $('.optical_prescription').text("Prescription");
        	this._super(force_validation);
        },
    });


});
