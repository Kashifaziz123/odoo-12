from odoo import models, api


class ProductFromPos(models.Model):
    _inherit = 'dr.prescription'

    @api.model
    def create_product_pos(self, vals):
        prescription_type = None
        if vals.get('prescription_type') == 'Internal':
            prescription_type = 'internal'
        elif vals.get('prescription_type') == 'External':
            prescription_type = 'external'

        od_sph_distance= None
        if vals.get('od_sph_distance') == '-8.00':
            od_sph_distance = '-8.00'
        elif vals.get('od_sph_distance') == '-7.75':
            od_sph_distance = '-7.75'

        od_cyl_distance = None
        if vals.get('od_cyl_distance') == '-3.50':
            od_cyl_distance = '-3.50'
        elif vals.get('od_cyl_distance') == '-3.25':
            od_cyl_distance = '-3.25'

        od_axis_distance = None
        if vals.get('od_axis_distance') == '1':
            od_axis_distance = '1'
        elif vals.get('od_axis_distance') == '2':
            od_axis_distance = '2'

        od_add_distance = None
        if vals.get('od_add_distance') == '0.00':
            od_add_distance = '-0.00'
        elif vals.get('od_add_distance') == '+0.25':
            od_add_distance = '+0.25'

        od_prism_distance = None
        if vals.get('od_prism_distance') == '0.25':
            od_prism_distance = '0.25'
        elif vals.get('od_prism_distance') == '0.50':
            od_prism_distance = '0.50'

        od_base_distance = None
        if vals.get('od_base_distance') == 'IN':
            od_base_distance = 'IN'
        elif vals.get('od_base_distance') == 'OUT':
            od_base_distance = 'OUT'
        elif vals.get('od_base_distance') == 'UP':
            od_base_distance = 'UP'
        elif vals.get('od_base_distance') == 'DOWN':
            od_base_distance = 'DOWN'

        os_sph_distance = None
        if vals.get('os_sph_distance') == '-8.00':
            os_sph_distance = '-8.00'
        elif vals.get('os_sph_distance') == '-7.75':
            os_sph_distance = '-7.75'

        # os_cyl_distance = None
        # if vals.get('os_cyl_distance') == '-8.00':
        #     os_cyl_distance = '-8.00'
        # elif vals.get('os_cyl_distance') == '-7.75':
        #     os_cyl_distance = '-7.75'





        doctor = self.env['optical.dr'].search([('name', '=', vals.get('doctor'))], limit=1)
        customer = self.env['res.partner'].search([('name', '=', vals.get('partner'))], limit=1)
        test_type = self.env['eye.test.type'].search([('name', '=', vals.get('test_type'))], limit=1)
        new_vals = {
            'dr': doctor.id if doctor else None,
            'customer': customer.id,
            'checkup_date':vals.get('checkup_date') if vals.get('checkup_date') else '',
            'test_type':test_type.id,
            'prescription_type':prescription_type if prescription_type else '',
            'eye_examination_chargeable': vals.get('eyes_charges') if vals.get('eyes_charges') else '',
            'family_eye_history': vals.get('eyes_history') if vals.get('eyes_history') else '',
            'ocular_history': vals.get('ocular_history') if vals.get('ocular_history') else '',
            'consultation': vals.get('consultation_reason') if vals.get('consultation_reason') else '',
            'diagnosis_client': vals.get('diagnosis_client') if vals.get('diagnosis_client') else '',
            'notes_laboratory': vals.get('notes_laboratory') if vals.get('notes_laboratory') else '',
            'optometrist_observation': vals.get('optometrist_observation') if vals.get('optometrist_observation') else '',
            'od_sph_distance':od_sph_distance if od_sph_distance else '',
            'od_cyl_distance':od_cyl_distance if od_cyl_distance else '',
            'od_ax_distance': od_axis_distance if od_axis_distance else '',
            'od_add_distance': od_add_distance  if od_add_distance  else '',
            'od_prism_distance': od_prism_distance if od_prism_distance else '',
            'od_base_distance': od_base_distance if od_base_distance else '',
            'os_sph_distance': os_sph_distance if os_sph_distance else '',
            # 'os_cyl_distance': os_cyl_distance if os_cyl_distance else ''
            # '': od_sph_distance if od_sph_distance else '',
            # '': od_sph_distance if od_sph_distance else '',
            # '': od_sph_distance if od_sph_distance else '',
            # '': od_sph_distance if od_sph_distance else '',



            }
        print(new_vals)
        rec = self.env['dr.prescription'].create(new_vals)
        new_vals['id'] = rec.id
        new_vals['dr'] = [rec.dr.id] if rec.dr else []
        new_vals['customer'] = [rec.customer.id] if rec.customer else []
        new_vals['test_type'] = [rec.test_type.id] if rec.test_type else []
        new_vals['checkup_date'] = rec.checkup_date if rec.checkup_date else ''
        new_vals['prescription_type'] = rec.prescription_type if rec.prescription_type else ''
        new_vals['eye_examination_chargeable'] = rec.eye_examination_chargeable if rec.eye_examination_chargeable else ''
        new_vals['family_eye_history'] = rec.family_eye_history if rec.family_eye_history else ''
        new_vals['ocular_history'] = rec.ocular_history if rec.ocular_history else ''
        new_vals['consultation'] = rec.consultation if rec.consultation else ''
        new_vals['diagnosis_client'] = rec.diagnosis_client if rec.diagnosis_client else ''
        new_vals['notes_laboratory'] = rec.notes_laboratory if rec.notes_laboratory else ''
        new_vals['optometrist_observation'] = rec.optometrist_observation if rec.optometrist_observation else ''
        new_vals['od_sph_distance'] = rec.od_sph_distance if rec.od_sph_distance else ''
        new_vals['od_cyl_distance'] = rec.od_cyl_distance if rec.od_cyl_distance else ''
        new_vals['od_ax_distance'] = rec.od_ax_distance if rec.od_ax_distance else ''
        new_vals['od_add_distance'] = rec.od_add_distance if rec.od_add_distance else ''
        new_vals['od_prism_distance'] = rec.od_prism_distance if rec.od_prism_distance else ''
        new_vals['od_base_distance'] = rec.od_base_distance if rec.od_base_distance else ''
        new_vals['os_sph_distance'] = rec.os_sph_distance if rec.os_sph_distance else ''
        # new_vals['os_cyl_distance'] = rec.os_cyl_distance if rec.os_cyl_distance else ''
        # new_vals[''] = rec. if rec. else ''

        return new_vals
