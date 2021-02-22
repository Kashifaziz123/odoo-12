odoo.define('pos_prescription_creation.db', function (require) {

	var DB = require('point_of_sale.DB');
	DB.include({
		init: function(options){
        	this._super.apply(this, arguments);
            this.optical_all_orders = {};
        	this.optical_order_by_name = {};
        },
        add_optical_orders: function(optical_orders){
            this.optical_all_orders.push(optical_orders);
            this.optical_order_by_name[optical_orders.name] = optical_orders;
        },
	});
});