# -*- coding: utf-8 -*-

from odoo import api, fields, models,_


class InheritedSaleOrder(models.Model):
    _inherit = 'sale.order'

    prescription_id = fields.Many2one('dr.prescription')
    doctor = fields.Char(related='prescription_id.dr.name')
    prescription_date = fields.Date(related='prescription_id.checkup_date')













