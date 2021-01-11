from odoo import api, fields, models,_

class InheritedUsers(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean()
    is_patient = fields.Boolean()

class InheritedSaleOrder(models.Model):
    _inherit = 'sale.order'

    prescription_id = fields.Many2one('dr.prescription')












