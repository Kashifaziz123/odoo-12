odoo.define('optical_erp.screens',function(require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const IndependentToOrderScreen = require('point_of_sale.IndependentToOrderScreen');

    //-----------------------------------------
    //-----------------------------------------
    // Prescription History Screen
    //-----------------------------------------
    //-----------------------------------------

    class PrescriptionListScreenWidget extends IndependentToOrderScreen {


    constructor() {
            super(...arguments);
//            this.$('.products-list-contents').on('click', '.productlines', function(event){
//                self.line_select(event,$(this),parseInt($(this).data('id')));
//            });
//            this.$('.searchbox_date').keyup(function() {
//                self.render_list(optical_orders, this.childNodes[1].value, undefined);
//            });
//            this.$('.searchbox_client').keyup(function() {
//                self.render_list(optical_orders, undefined, this.childNodes[1].value);
//            });
//            this.$('.searchbox .search-clear').click(function(){
//                self.clear_search();
//            });

    }
//            super(...arguments);
//            useListener('filter-selected', this._onFilterSelected);
//
//            useListener('search', this._onSearch);
//            this.searchDetails = {};
//            this.filter = null;
//            this._initializeSearchFieldConstants();
//
//
//            }

        mounted() {
            var self = this;
            this.render();
            var self = this;
            var optical_orders = [];
            var order = this.env.pos.get_order();
            var optical_order_ids = this.props.all_orders // order.get_screen_data('params')
            if (optical_order_ids)
                for (var i=0; i < optical_order_ids.length; i++)
                    optical_orders.push(self.env.pos.optical.order_by_id[optical_order_ids[i].id])
            else
                var optical_orders = self.env.pos.optical.all_orders
            this.render_list(optical_orders, undefined, undefined);
            var search_timeout = null;
        }

        back() {
            this.close();
        }

        render_list(optical_orders, date_value, client_value){
            var self = this
            var length = optical_orders.length
            var contents = this.el.querySelector('.products-list-contents');
            contents.innerHTML = "";
            if (client_value)
                optical_orders = optical_orders.filter(function(el){return el.customer[1].toLowerCase().includes(client_value.toLowerCase())})
            if (date_value)
                optical_orders = optical_orders.filter(function(el){return el.checkup_date.toLowerCase().includes(date_value.toLowerCase())})
            var len = Math.min(optical_orders.length)-1;
            for(var i = len ; i >= 0; i--){
                var optical_order = optical_orders[i];
                var optical_orders_line_html = this.env.qweb.render('PrescriptionHistoryScreenData',{widget: this, product:optical_order});
                var optical_orders_line = document.createElement('tbody');
                optical_orders_line.innerHTML = optical_orders_line_html;
                optical_orders_line = optical_orders_line.childNodes[1];
                contents.appendChild(optical_orders_line);
            }
            this.$('.pos_optical_copy').click(function(event) {
                var order = self.env.pos.get_order();
                optical_order = self.env.pos.optical.order_by_id[parseInt($(this).data('orderId'))];
                $('.optical_prescription').text(optical_order.name);
                order.set_optical_reference(optical_order);
                this.close();
            });
            this.$('.pos_optical_print').click(function(event) {
                self.gui.show_screen('PrescriptionReceipt',parseInt($(this).data('orderId')));
            });
        }


}

    PrescriptionListScreenWidget.template = 'PrescriptionHistoryScreenContainer';
    Registries.Component.add(PrescriptionListScreenWidget);
    return PrescriptionListScreenWidget;

});