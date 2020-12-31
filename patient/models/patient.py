# -*- coding: utf-8 -*-

from odoo import api, fields, models,_
from odoo.exceptions import UserError


class Patient(models.Model):
    _name = "optical.patient"
    _inherits = {
        'res.partner':'partner_id',
    }
    create_users_button= fields.Boolean()
    # user_id = fields.Many2one('res.users')
    partner_id = fields.Many2one('res.partner', string='Related Partner', required=True,ondelete='restrict',help='Partner-related data of the Doctor')
    is_patient = fields.Boolean()

    def create_patient(self):
        self.is_patient=True
        if len(self.partner_id.user_ids):
            raise UserError(_('User for this patient already created.'))
        else:
            self.create_users_button = False
        patient_id = []

        patient_id.append(self.env['res.groups'].search([('name','=','Patient')]).id)
        patient_id.append(self.env['res.groups'].search([('name', '=','Internal User')]).id)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Name ',
            'view_mode': 'form',
            'view_id': self.env.ref("patient.view_create_user_wizard_form").id,
            'target': 'new',
            'res_model': 'res.users',
            'context': {'default_partner_id':self.partner_id.id,'default_is_patient':True,'default_groups_id':[(6,0,patient_id)]}

        }


