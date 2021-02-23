/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
/* See LICENSE file for full copyright and licensing details. */
/* License URL : <https://store.webkul.com/license.html/> */
odoo.define('pos_orders.pos_orders',function(require){
    "use strict"
    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var QWeb = core.qweb;
    var SuperPosModel = models.PosModel.prototype;
    var pos = require('point_of_sale.models');

    models.load_models([{
            model: 'pos.order',
            fields: ['id', 'name', 'date_order', 'session_id', 'partner_id', 'lines', 'ean13', 'sales_person_id',  'pos_reference', 'account_move', 'user_id', 'amount_paid', 'amount_total', 'amount_tax', 'state'],
            domain: function(self) {
                var domain_list = [];
                if(self.config.order_loading_options == 'n_days'){
                    var today = new Date();
                    var validation_date = new Date(today.setDate(today.getDate()-self.config.number_of_days)).toISOString();
                    domain_list = [['date_order','>',validation_date],['state', 'not in', ['draft', 'cancel']]];
                }
                else if(self.config.order_loading_options == 'current_session')
                    domain_list = [['session_id', '=', self.pos_session.name], ['state', 'not in', ['draft', 'cancel']]];
                else
                    domain_list = [['state', 'not in', ['draft', 'cancel']]];
                return domain_list;
            },
            loaded: function(self, wk_order) {
                self.db.pos_all_orders = wk_order;
                self.db.order_by_id = {};
                wk_order.forEach(function(order){
                    var order_date = new Date(order['date_order']);
                    var utc = order_date.getTime() - (order_date.getTimezoneOffset() * 60000);
                    order['date_order'] = new Date(utc).toLocaleString();
                    self.db.order_by_id[order.id] = order;
                });
            },
        }, {
            model: 'pos.order.line',
            fields: ['product_id', 'order_id', 'qty','discount','price_unit','price_subtotal_incl','price_subtotal','sales_person_id'],
            domain: function(self) {
                var order_lines = []
                var orders = self.db.pos_all_orders;
                for (var i = 0; i < orders.length; i++) {
                    order_lines = order_lines.concat(orders[i]['lines']);
                }
                return [
                    ['id', 'in', order_lines]
                ];
            },
            loaded: function(self, wk_order_lines) {
                self.db.pos_all_order_lines = wk_order_lines;
                self.db.line_by_id = {};
                wk_order_lines.forEach(function(line){
                    self.db.line_by_id[line.id] = line;
                });
            },
        }, ], {
        'after': 'product.product'
    });

    models.PosModel = models.PosModel.extend({
        _save_to_server: function (orders, options) {
            var self = this;
            return SuperPosModel._save_to_server.call(this,orders,options).then(function(return_dict){
                if(return_dict.orders != null){
                    return_dict.orders.forEach(function(order){
                        if(order.existing)
                        {
                            self.db.pos_all_orders.forEach(function(order_from_list){
                                if(order_from_list.id == order.original_order_id)
                                    order_from_list.return_status = order.return_status
                            });
                        }
                        else{
                            var order_date = new Date(order['date_order'])
                            var utc = order_date.getTime() - (order_date.getTimezoneOffset() * 60000);
                            order['date_order'] = new Date(utc).toLocaleString()
                            self.db.pos_all_orders.unshift(order);
                            self.db.order_by_id[order.id] = order;
                        }
                    });
                    return_dict.orderlines.forEach(function(orderline){
                        if(orderline.existing){
                            var target_line = self.db.line_by_id[orderline.id];
                            target_line.line_qty_returned = orderline.line_qty_returned;
                        }
                        else{
                            self.db.pos_all_order_lines.unshift(orderline);
                            self.db.line_by_id[orderline.id] = orderline;
                        }
                    });
                    if(self.db.all_payments)
                        return_dict.payments.forEach(function(payment) {
                            self.db.all_payments.unshift(payment);
                            self.db.payment_by_id[payment.id] = payment;
                    });

                }
                return return_dict.order_ids;
            });
        }
    });

    //For Re-Print Order Receipt
    screens.ReceiptScreenWidget.include({
        render_receipt: function() {
            if (!this.pos.reloaded_order) {
                return this._super();
            }
            var order = this.pos.reloaded_order;
            this.$('.pos-receipt-container').html(QWeb.render('OrderReceipt', {
                widget: this,
                pos: this.pos,
                order: order,
                receipt: order.export_for_printing(),
                orderlines: order.get_orderlines(),
                paymentlines: order.get_paymentlines(),
            }));
            this.pos.from_loaded_order = true;
        },
        click_next: function() {
            if (!this.pos.from_loaded_order) {
                return this._super();
            }
            this.pos.from_loaded_order = false;
            // When reprinting a loaded order we temporarily set it as the
            // active one. When we get out from the printing screen, we set
            // it back to the one that was active
            if (this.pos.current_order) {
                this.pos.set_order(this.pos.current_order);
                this.pos.current_order = false;
            }
            return this.gui.show_screen(this.gui.startup_screen);
        },
    });

    var OrdersScreenWidget = screens.ScreenWidget.extend({
        template: 'OrdersScreenWidget',

        init: function(parent, options) {
            this._super(parent, options);
        },
        get_customer: function(customer_id){
            var self = this;
            if(self.gui)
                return self.gui.get_current_screen_param('customer_id');
            else
                return undefined;
        },
        render_list: function(order, input_txt) {
            var self = this;
            var customer_id = this.get_customer();
            var new_order_data = [];
            if(customer_id != undefined){
                for(var i=0; i<order.length; i++){
                    if(order[i].partner_id[0] == customer_id)
                        new_order_data = new_order_data.concat(order[i]);
                }
                order = new_order_data;
            }
            if (input_txt != undefined && input_txt != '') {
                var new_order_data = [];
                var search_text = input_txt.toLowerCase()
                for (var i = 0; i < order.length; i++) {
                    if (order[i].partner_id == '') {
                        order[i].partner_id = [0, '-'];
                    }
                    if (((order[i].name.toLowerCase()).indexOf(search_text) != -1) || ((order[i].pos_reference.toLowerCase()).indexOf(search_text) != -1) || ((order[i].partner_id[1].toLowerCase()).indexOf(search_text) != -1)) {
                        new_order_data = new_order_data.concat(order[i]);
                    }
                }
                order = new_order_data;
            }
            var contents = this.$el[0].querySelector('.wk-order-list-contents');
            contents.innerHTML = "";
            var wk_orders = order;
            for (var i = 0, len = Math.min(wk_orders.length, 1000); i < len; i++) {
                var wk_order = wk_orders[i];
                var orderline_html = QWeb.render('WkOrderLine', {
                    widget: this,
                    order: wk_orders[i],
                    customer_id:wk_orders[i].partner_id[0],
                });
                var orderline = document.createElement('tbody');
                orderline.innerHTML = orderline_html;
                orderline = orderline.childNodes[1];
                contents.appendChild(orderline);
            }

            //For Re-Print Order Receipt
            this.$('.wk_print_content').click(function(event) {
                self.order_list_actions_wk(event, 'print');
            });
        },

        show: function() {
            var self = this;
            this._super();
            var orders = self.pos.db.pos_all_orders;
            this.render_list(orders, undefined);
            this.$('.order_search').keyup(function() {
            self.render_list(orders, this.value);});
            this.$('.back').on('click',function() {
                self.gui.show_screen('products');
            });
            //For Re-Print Order Receipt
            this.old_order = this.pos.get_order();
        },
        close: function() {
            this._super();
            this.$('.wk-order-list-contents').undelegate();
        },

        //For Re-Print Order Receipt
        order_list_actions_wk: function(event, action) {
            var self = this;
            var dataset = event.target.parentNode.dataset;
            self.load_order_data_wk(parseInt(dataset.orderId, 10))
                .then(function(order_data) {
                    self.order_action_wk(order_data, action);
                });
        },

        //For Re-Print Order Receipt
        order_action_wk: function(order_data, action) {
            if (this.old_order !== null) {
                this.gui.back();
            }
            var order = this.load_order_from_data_wk(order_data, action);
            if (!order) {
                // The load of the order failed. (products not found, ...
                // We cancel the action
                return;
            }
            this['action_' + action](order_data, order);
        },

        //For Re-Print Order Receipt
        action_print: function(order_data, order) {
            // We store temporarily the current order so we can safely compute
            // taxes based on fiscal position
            this.pos.current_order = this.pos.get_order();

            this.pos.set_order(order);

            if (this.pos.config.iface_print_via_proxy) {
                this.pos.proxy.print_receipt(QWeb.render(
                    'OrderReceipt', {
                        widget: this,
                        pos: this.pos,
                        order: order,
                        receipt: order.export_for_printing(),
                        orderlines: order.get_orderlines(),
                        paymentlinesf: order.get_paymentlines(),
                    }));
                this.pos.set_order(this.pos.current_order);
                this.pos.current_order = false;
            } else {
                this.pos.reloaded_order = order;
                this.gui.show_screen('receipt');
                this.pos.reloaded_order = false;
            }

            // If it's invoiced, we also print the invoice
            if (order_data.to_invoice) {
                this.pos.chrome.do_action('point_of_sale.pos_invoice_report', {
                    additional_context: {
                        active_ids: [order_data.id]
                    }
                })
            }

            // Destroy the order so it's removed from localStorage
            // Otherwise it will stay there and reappear on browser refresh
            order.destroy();
        },

        //For Re-Print Order Receipt
        _prepare_order_from_order_data_wk: function(order_data, action) {
            var self = this;
            var order = new pos.Order({}, {
                pos: this.pos,
            });

            // Get Customer
            if (order_data.partner_id) {
                order.set_client(
                    this.pos.db.get_partner_by_id(order_data.partner_id));
            }

            // Get fiscal position
            if (order_data.fiscal_position && this.pos.fiscal_positions) {
                var fiscal_positions = this.pos.fiscal_positions;
                order.fiscal_position = fiscal_positions.filter(function(p) {
                    return p.id === order_data.fiscal_position;
                })[0];
                order.trigger('change');
            }

            // Get order lines
            self._prepare_orderlines_from_order_data_wk(
                order, order_data, action);

            // Get order data
            if (['print'].indexOf(action) !== -1) {
                order.ean13 = order_data.ean13;
                order.sales_person_id = order_data.sales_person_id;
                order.name = order_data.pos_reference;
                order.formatted_validation_date = moment(order_data.date_order).format('DD/MM/YYYY HH:mm:ss');
            }

            // Get Payment lines
            if (['print'].indexOf(action) !== -1) {
                var paymentLines = order_data.payment_lines || [];
                _.each(paymentLines, function(paymentLine) {
                    var line = paymentLine;
                    // In case of local data
                    if (line.length === 3) {
                        line = line[2];
                    }
                    _.each(self.pos.payment_methods, function(payment_method) {
                        if (payment_method.id === line.payment_method_id) {
                            if (line.amount > 0) {
                                // If it is not change
                                order.add_paymentline(payment_method);
                                order.selected_paymentline.set_amount(
                                    line.amount);
                            }
                        }
                    });
                });
            }
            return order;
        },

        //For Re-Print Order Receipt
        _prepare_orderlines_from_order_data_wk: function(
            order, order_data, action) {
            var orderLines = order_data.line_ids || order_data.lines || [];

            var self = this;
            _.each(orderLines, function(orderLine) {
                var line = orderLine;
                // In case of local data
                if (line.length === 3) {
                    line = line[2];
                }
                var product = self.pos.db.get_product_by_id(line.product_id);
                // Check if product are available in pos
                if (_.isUndefined(product)) {
                    self.unknown_products.push(String(line.product_id));
                } else {
                    var qty = line.qty;
                    if (['return'].indexOf(action) !== -1) {
                        // Invert line quantities
                        qty *= -1;
                    }
                    // Create a new order line
                    order.add_product(product, {
                        price: line.price_unit,
                        quantity: qty,
                        discount: line.discount,
                        merge: false,
                    });
                }
            });
        },

        //For Re-Print Order Receipt
        load_order_data_wk: function(order_id) {
            var self = this;
            return this._rpc({
                model: 'pos.order',
                method: 'load_done_order_for_pos_wk',
                args: [order_id],
            }).guardedCatch(function(reason) {
                if (parseInt(reason.message.code, 10) === 200) {
                    // Business Logic Error, not a connection problem
                    self.gui.show_popup(
                        'error-traceback', {
                            'title': error.data.message,
                            'body': error.data.debug,
                        }
                    );
                } else {
                    self.gui.show_popup('error', {
                        'title': _t('Connection error'),
                        'body': _t(
                            'Can not execute this action because the POS' +
                            ' is currently offline'),
                    });
                }
            });
        },

        //For Re-Print Order Receipt
        load_order_from_data_wk: function(order_data, action) {
            var self = this;
            this.unknown_products = [];
            var order = self._prepare_order_from_order_data_wk(
                order_data, action);
            // Forbid POS Order loading if some products are unknown
            if (self.unknown_products.length > 0) {
                self.gui.show_popup('error-traceback', {
                    'title': _t('Unknown Products'),
                    'body': _t('Unable to load some order lines because the ' +
                            'products are not available in the POS cache.\n\n' +
                            'Please check that lines :\n\n  * ') +
                        self.unknown_products.join("; \n  *"),
                });
                return false;
            }
            return order;
        },

    });
    gui.define_screen({name: 'wk_order',widget:OrdersScreenWidget});

	// Start AllOrdersButtonWidget
	var AllOrdersButtonWidget = screens.ActionButtonWidget.extend({
		template: 'AllOrdersButtonWidget',

		button_click: function() {
			var self = this;
			this.gui.show_screen('wk_order', {});
		},

	});

	screens.define_action_button({
		'name': 'All Orders Button Widget',
		'widget': AllOrdersButtonWidget,
		'condition': function() {
			return true;
		},
	});
	// End SeeAllOrdersButtonWidget
	
/*     screens.ProductScreenWidget.include({
        show: function(){
            var self = this;
            this._super();
            this.product_categories_widget.reset_category();
            this.numpad.state.reset();
            $('#all_orders').on('click',function(){
                self.gui.show_screen('wk_order',{});
            });
        },
    }); */
    screens.ClientListScreenWidget.include({
        show: function() {
            var self = this;
            self._super();
            $('.view_all_order').on('click',function() {
                self.gui.show_screen('wk_order',{
                    'customer_id':this.id
                });
            });
        }
    });
    return OrdersScreenWidget;
});
