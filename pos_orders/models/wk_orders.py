# -*- coding: utf-8 -*-
#################################################################################
#
#   Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#   See LICENSE file for full copyright and licensing details.
#   License URL : <https://store.webkul.com/license.html/>
# 
#################################################################################
from odoo import api, fields, models
from odoo.exceptions import Warning,ValidationError

class PosOrder(models.Model):
    _inherit = 'pos.order'

    # @api.model
    # def create_from_ui(self,orders,draft=False):
        # order_ids = super(PosOrder,self).create_from_ui(orders,draft=False)
        
        # my_order_ids = [ sub['id'] for sub in order_ids ]
        # order_objs = self.env['pos.order'].browse(my_order_ids)
        # result = {}
        # order_list = []
        # order_line_list = []
        # payment_list = []
        # for order_obj in order_objs:
            # vals = {}
            # vals['lines'] = []
            # if hasattr(order_objs[0], 'return_status'):
                # if not order_obj.is_return_order:
                    # vals['return_status'] = order_obj.return_status
                    # vals['existing'] = False
                    # vals['id'] = order_obj.id
                # else:
                    # order_obj.return_order_id.return_status = order_obj.return_status
                    # vals['existing'] = True
                    # vals['id'] = order_obj.id
                    # vals['original_order_id'] = order_obj.return_order_id.id
                    # vals['return_status'] = order_obj.return_order_id.return_status
                    # for line in order_obj.lines:
                        # line_vals = {}
                        # if line.original_line_id:
                            # line_vals['id'] = line.original_line_id.id
                            # line_vals['line_qty_returned'] = line.original_line_id.line_qty_returned
                            # line_vals['existing'] = True
                        # order_line_list.append(line_vals)
            # vals['payment_ids'] = order_obj.payment_ids.ids
            # vals['name'] = order_obj.name
            # vals['sales_person_id'] = [order_obj.sales_person_id.id, order_obj.sales_person_id.name]
            # vals['ean13'] = order_obj.ean13
            # vals['amount_tax'] = order_obj.amount_tax
            # vals['amount_total'] = order_obj.amount_total
            # vals['amount_paid'] = order_obj.amount_paid
            # vals['pos_reference'] = order_obj.pos_reference
            # vals['date_order'] = order_obj.date_order
            # vals['session_id'] = [order_obj.session_id.id, order_obj.session_id.name]
            # vals['user_id'] = [order_obj.user_id.id, order_obj.user_id.name]
            # vals['state'] = order_obj.state
            # if order_obj.account_move:
                # vals['account_move'] = order_obj.account_move.id
            # else:
                # vals['account_move'] = False
            # if order_obj.partner_id:
                # vals['partner_id'] = [order_obj.partner_id.id, order_obj.partner_id.name]
            # else:
                # vals['partner_id'] = False
            # if (not hasattr(order_objs[0], 'return_status') or (hasattr(order_objs[0], 'return_status') and not order_obj.is_return_order)):
                # vals['id'] = order_obj.id
                # for line in order_obj.lines:
                    # vals['lines'].append(line.id)
                    # line_vals = {}
                    # # LINE DATAA
                    # line_vals['create_date'] = line.create_date
                    # line_vals['discount'] = line.discount
                    # line_vals['display_name'] = line.display_name
                    # line_vals['id'] = line.id
                    # line_vals['order_id'] = [line.order_id.id, line.order_id.name]
                    # line_vals['price_subtotal'] = line.price_subtotal
                    # line_vals['price_subtotal_incl'] = line.price_subtotal_incl
                    # line_vals['price_unit'] = line.price_unit
                    # line_vals['product_id'] = [line.product_id.id, line.product_id.name]
                    # line_vals['qty'] = line.qty
                    # line_vals['write_date'] = line.write_date
                    # line_vals['sales_person_id'] = [line.sales_person_id.id, line.sales_person_id.name]
                    # if hasattr(line, 'line_qty_returned'):
                        # line_vals['line_qty_returned'] = line.line_qty_returned
                    # # LINE DATAA
                    # order_line_list.append(line_vals)
                # for payment_line in order_obj.payment_ids:
                    # payment_vals = {}
                    # # PAYMENT DATA
                    # payment_vals['amount'] = payment_line.amount
                    # payment_vals['payment_method_id'] = [payment_line.payment_method_id.id, payment_line.payment_method_id.name]
                    # payment_vals['id'] = payment_line.id

                    # payment_list.append(payment_vals)
            # order_list.append(vals)
        # result['orders'] = order_list
        # result['orderlines'] = order_line_list
        # result['payments'] = payment_list
        # result['order_ids'] = order_ids
        # return result

    #For Re-Print Order Receipt
    def _prepare_done_order_for_pos_wk(self):
        # self.ensure_one()
        order_lines = []
        payment_lines = []
        for order_line in self.lines:
            order_line = self._prepare_done_order_line_for_pos_wk(order_line)
            order_lines.append(order_line)
        for payment_line in self.payment_ids:
            payment_line = self._prepare_done_order_payment_for_pos_wk(
                payment_line)
            payment_lines.append(payment_line)
        res = {
            'id': self.id,
            'date_order': self.date_order,
            'pos_reference': self.pos_reference,
            'name': self.name,
            'partner_id': self.partner_id.id,
            'fiscal_position': self.fiscal_position_id.id,
            'line_ids': order_lines,
            'payment_lines': payment_lines,
            'to_invoice': bool(self.account_move),
            'ean13': self.ean13,
            'sales_person_id': self.sales_person_id.id,
        }
        return res

    #For Re-Print Order Receipt
    def _prepare_done_order_line_for_pos_wk(self, order_line):
        # self.ensure_one()
        return {
            'product_id': order_line.product_id.id,
            'qty': order_line.qty,
            'price_unit': order_line.price_unit,
            'discount': order_line.discount,
        }

    #For Re-Print Order Receipt
    def _prepare_done_order_payment_for_pos_wk(self, payment_line):
        # self.ensure_one()
        return {
            'payment_method_id': payment_line.payment_method_id.id,
            'amount': payment_line.amount,
        }

    #For Re-Print Order Receipt
    def load_done_order_for_pos_wk(self):
        # self.ensure_one()
        return self._prepare_done_order_for_pos_wk()


class PosConfig(models.Model):
    _inherit = 'pos.config'

    order_loading_options = fields.Selection([("current_session","Load Orders Of Current Session"), ("all_orders","Load All Past Orders"), ("n_days","Load Orders Of Last 'n' Days")], default='current_session', string="Loading Options")
    number_of_days = fields.Integer(string='Number Of Past Days',default=10)

    @api.constrains('number_of_days')
    def number_of_days_validation(self):
        if self.order_loading_options == 'n_days':
            if not self.number_of_days or self.number_of_days < 0:
                raise ValidationError("Please provide a valid value for the field 'Number Of Past Days'!!!")
