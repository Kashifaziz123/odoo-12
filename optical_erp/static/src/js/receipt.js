odoo.define('pos_prescription_creation.receipt', function(require){

    var core = require('web.core');
    var QWeb = core.qweb;
	var gui = require('point_of_sale.gui');
	var screens = require('point_of_sale.screens');

    // For Prescription Receipt
    var PrintPrescriptionScreenWidget = screens.ReceiptScreenWidget.extend({
        template: 'PrintPrescriptionScreenWidget',
        get_receipt_render_env: function() {
            var order = this.pos.get_order();
            var optical_order = this.pos.optical.order_by_id[order.get_screen_data('params')]
            return {
                widget: this,
                pos: this.pos,
                order: order,
                optical_order: optical_order,
                receipt: order.export_for_printing(),
                orderlines: order.get_orderlines(),
                paymentlines: order.get_paymentlines(),
            };
        },
        print_html: function () {
            var receipt = QWeb.render('PrescriptionOrderReceipt', this.get_receipt_render_env());
            this.pos.proxy.printer.print_receipt(receipt);
            this.pos.get_order()._printed = true;
        },
        click_back: function() {
           this._super();
           this.gui.show_screen('products');
        },
        render_receipt: function() {
            this.$('.pos-receipt-container').html(QWeb.render('PrescriptionOrderReceipt', this.get_receipt_render_env()));
        },
    });
    gui.define_screen({name:'PrescriptionReceipt', widget: PrintPrescriptionScreenWidget});

    // For POS Receipt
    screens.ReceiptScreenWidget.include({
        render_receipt: function() {
            if (!this.pos.reloaded_order) {
                return this._super();
            }
            var order = this.pos.reloaded_order;
            optical_order = [];
            if (order.optical_reference){
                if (order.optical_reference.id)
                    var optical_order = this.pos.optical.order_by_id[order.optical_reference.id]
                else
                    var optical_order = this.pos.optical.order_by_id[order.optical_reference]
            }
            this.$('.pos-receipt-container').html(QWeb.render('OrderReceipt', {
                widget: this,
                pos: this.pos,
                order: order,
                optical_order: optical_order,
                receipt: order.export_for_printing(),
                orderlines: order.get_orderlines(),
                paymentlines: order.get_paymentlines(),
            }));
            this.pos.from_loaded_order = true;
        },
        get_receipt_render_env: function() {
            var order = this.pos.get_order();
            optical_order = [];
            if (order.optical_reference){
                if (order.optical_reference.id)
                    var optical_order = this.pos.optical.order_by_id[order.optical_reference.id]
                else
                    var optical_order = this.pos.optical.order_by_id[order.optical_reference]
            }
            else
                optical_order = 0;
            return {
                widget: this,
                pos: this.pos,
                order: order,
                optical_order: optical_order,
                receipt: order.export_for_printing(),
                orderlines: order.get_orderlines(),
                paymentlines: order.get_paymentlines(),
            };
        },
    });
});