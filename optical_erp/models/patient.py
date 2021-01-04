from odoo import api, fields, models,_

class InheritedDoctor(models.Model):
    _inherit = 'optical.patient'

    prescription_count = fields.Integer(compute='get_prescription_count')

    def get_prescription_count(self):
        count = self.env['dr.prescription'].search_count([('patient', '=', self.id)])
        self.prescription_count = count


    def open_doctor_prescriptions(self):
        for records in self:
            return {
                'name':_('Doctor Prescription'),
                'view_type': 'form',
                'domain': [('patient','=',records.id)],
                'res_model': 'dr.prescription',
                'view_id': False,
                'view_mode':'tree,form',
                # 'context':{'default_patient':self.id},
                'type': 'ir.actions.act_window',
            }

    def get_prescription_count(self):
        for records in self:
            count = self.env['dr.prescription'].search_count([('patient','=',records.id)])
            records.prescription_count = count



