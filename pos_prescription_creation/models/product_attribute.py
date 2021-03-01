# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    Sequence = fields.Integer(string="Sequence")
