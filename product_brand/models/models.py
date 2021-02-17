# -*- coding: utf-8 -*-
from addons.website import tools
from odoo import models, fields, api,_


class ModelBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brand'
    _order = 'name asc'

    name = fields.Char('Brand Name')
    brand_ids = fields.One2many('product.template','brand_id', string='Order Lines')
    brand_image = fields.Binary("Logo", attachment=True,help="This field holds the image used as logo for the brand, limited to 1024x1024px.")


class InheritedProductTemplate(models.Model):
    _inherit = 'product.template'

    brand_id = fields.Many2one('product.brand')



