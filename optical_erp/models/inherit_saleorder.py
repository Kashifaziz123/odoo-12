# -*- coding: utf-8 -*-

from odoo import api, fields, models,_


class InheritedSaleOrder(models.Model):
    _inherit = 'sale.order'

    prescription_id = fields.Many2one('dr.prescription')












