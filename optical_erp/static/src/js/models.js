odoo.define('pos_prescription_creation.models', function(require){

	var chrome = require('point_of_sale.chrome');
	var screens = require('point_of_sale.screens');


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
