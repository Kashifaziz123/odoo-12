# -*- coding: utf-8 -*-

from odoo import api, fields, models,_


class InheritedUsers(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean()
    is_patient = fields.Boolean()














