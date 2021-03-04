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
                var optical_reference = this.pos.optical.order_by_id[json.optical_reference];
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
                optical_reference = this.optical.order_by_id[order.optical_reference.id]
                return optical_reference;
            }
            return null;
        },
        delete_current_order: function(){
            var order = this.get_order();
            if (order) {
                order.destroy({'reason':'abandon'});
            }
            $('.optical_prescription').text("Prescription")
        },
    });

    chrome.OrderSelectorWidget.include({
        order_click_handler: function(event,$el) {
            this._super(event,$el);
            var order = this.pos.get_order();
            if (order!==null && order!==undefined && order.optical_reference)
                $('.optical_prescription').text(order.optical_reference.name)
            else
                $('.optical_prescription').text("Prescription")
        },

        neworder_click_handler: function(event, $el) {
            this._super(event, $el);
            $('.optical_prescription').text("Prescription")
        },

        deleteorder_click_handler: function(event,$el) {
            this._super(event,$el);
            var order = this.pos.get_order();
            if (order!==null && order!==undefined && order.optical_reference)
                $('.optical_prescription').text(order.optical_reference.name)
            else
                $('.optical_prescription').text("Prescription")
        },
    });

	screens.PaymentScreenWidget.include({
        validate_order: function(force_validation){
            $('.optical_prescription').text("Prescription");
        	this._super(force_validation);
        },
    });
});
