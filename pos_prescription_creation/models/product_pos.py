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
        if vals.get('od_sph_distance') == '0.00':
            od_sph_distance = '0.00'
        elif vals.get('od_sph_distance') == '-16.00':
            od_sph_distance = '-16.00'

        elif vals.get('od_sph_distance') == '-15.75':
            od_sph_distance = '-15.75'
        elif vals.get('od_sph_distance') == '15.50':
            od_sph_distance = '15.50'
        elif vals.get('od_sph_distance') == '-15.25':
            od_sph_distance = '-15.25'
        elif vals.get('od_sph_distance') == '-15.00':
            od_sph_distance = '-15.00'

        elif vals.get('od_sph_distance') == '-14.75':
            od_sph_distance = '-14.75'
        elif vals.get('od_sph_distance') == '14.50':
            od_sph_distance = '14.50'
        elif vals.get('od_sph_distance') == '-14.25':
            od_sph_distance = '-14.25'
        elif vals.get('od_sph_distance') == '-14.00':
            od_sph_distance = '-14.00'

        elif vals.get('od_sph_distance') == '-13.75':
            od_sph_distance = '-13.75'
        elif vals.get('od_sph_distance') == '13.50':
            od_sph_distance = '13.50'
        elif vals.get('od_sph_distance') == '-13.25':
            od_sph_distance = '-13.25'
        elif vals.get('od_sph_distance') == '-13.00':
            od_sph_distance = '-13.00'

        elif vals.get('od_sph_distance') == '-12.75':
            od_sph_distance = '-12.75'
        elif vals.get('od_sph_distance') == '12.50':
            od_sph_distance = '12.50'
        elif vals.get('od_sph_distance') == '-12.25':
            od_sph_distance = '-12.25'
        elif vals.get('od_sph_distance') == '-12.00':
            od_sph_distance = '-12.00'

        elif vals.get('od_sph_distance') == '-11.75':
            od_sph_distance = '-11.75'
        elif vals.get('od_sph_distance') == '11.50':
            od_sph_distance = '11.50'
        elif vals.get('od_sph_distance') == '-11.25':
            od_sph_distance = '-11.25'
        elif vals.get('od_sph_distance') == '-11.00':
            od_sph_distance = '-11.00'

        elif vals.get('od_sph_distance') == '-10.75':
            od_sph_distance = '-10.75'
        elif vals.get('od_sph_distance') == '-10.50':
            od_sph_distance = '-10.50'
        elif vals.get('od_sph_distance') == '-10.25':
            od_sph_distance = '-10.25'
        elif vals.get('od_sph_distance') == '-10.00':
            od_sph_distance = '-10.00'

        elif vals.get('od_sph_distance') == '-9.75':
            od_sph_distance = '-9.75'
        elif vals.get('od_sph_distance') == '-9.50':
            od_sph_distance = '-9.50'
        elif vals.get('od_sph_distance') == '-9.25':
            od_sph_distance = '-9.25'
        elif vals.get('od_sph_distance') == '-9.00':
            od_sph_distance = '-9.00'

        elif vals.get('od_sph_distance') == '-8.75':
            od_sph_distance = '-8.75'
        elif vals.get('od_sph_distance') == '-8.50':
            od_sph_distance = '-8.50'
        elif vals.get('od_sph_distance') == '-8.25':
            od_sph_distance = '-8.25'
        elif vals.get('od_sph_distance') == '-8.00':
            od_sph_distance = '-8.00'

        elif vals.get('od_sph_distance') == '-7.75':
            od_sph_distance = '-7.75'
        elif vals.get('od_sph_distance') == '-7.50':
            od_sph_distance = '-7.50'
        elif vals.get('od_sph_distance') == '-7.25':
            od_sph_distance = '-7.25'
        elif vals.get('od_sph_distance') == '-7.00':
            od_sph_distance = '-7.00'

        elif vals.get('od_sph_distance') == '-6.75':
            od_sph_distance = '-6.75'
        elif vals.get('od_sph_distance') == '-6.50':
            od_sph_distance = '-6.50'
        elif vals.get('od_sph_distance') == '-6.25':
            od_sph_distance = '-6.25'
        elif vals.get('od_sph_distance') == '-6.00':
            od_sph_distance = '-6.00'

        elif vals.get('od_sph_distance') == '-5.75':
            od_sph_distance = '-5.75'
        elif vals.get('od_sph_distance') == '-5.50':
            od_sph_distance = '-5.50'
        elif vals.get('od_sph_distance') == '-5.25':
            od_sph_distance = '-5.25'
        elif vals.get('od_sph_distance') == '-5.00':
            od_sph_distance = '-5.00'

        elif vals.get('od_sph_distance') == '-4.75':
            od_sph_distance = '-4.75'
        elif vals.get('od_sph_distance') == '-4.50':
            od_sph_distance = '-4.50'
        elif vals.get('od_sph_distance') == '-4.25':
            od_sph_distance = '-4.25'
        elif vals.get('od_sph_distance') == '-4.00':
            od_sph_distance = '-4.00'

        elif vals.get('od_sph_distance') == '-3.75':
            od_sph_distance = '-3.75'
        elif vals.get('od_sph_distance') == '-3.50':
            od_sph_distance = '-3.50'
        elif vals.get('od_sph_distance') == '-3.25':
            od_sph_distance = '-3.25'
        elif vals.get('od_sph_distance') == '-3.00':
            od_sph_distance = '-3.00'

        elif vals.get('od_sph_distance') == '-2.75':
            od_sph_distance = '-2.75'
        elif vals.get('od_sph_distance') == '-2.50':
            od_sph_distance = '-2.50'
        elif vals.get('od_sph_distance') == '-2.25':
            od_sph_distance = '-2.25'
        elif vals.get('od_sph_distance') == '-2.00':
            od_sph_distance = '-2.00'

        elif vals.get('od_sph_distance') == '-1.75':
            od_sph_distance = '-1.75'
        elif vals.get('od_sph_distance') == '-1.50':
            od_sph_distance = '-1.50'
        elif vals.get('od_sph_distance') == '-1.25':
            od_sph_distance = '-1.25'
        elif vals.get('od_sph_distance') == '-1.00':
            od_sph_distance = '-1.00'

        elif vals.get('od_sph_distance') == '-0.75':
            od_sph_distance = '-0.75'
        elif vals.get('od_sph_distance') == '-0.50':
            od_sph_distance = '-0.50'
        elif vals.get('od_sph_distance') == '-0.25':
            od_sph_distance = '-0.25'
        elif vals.get('od_sph_distance') == '-0.00':
            od_sph_distance = '-0.00'

        elif vals.get('od_sph_distance') == '+0.75':
            od_sph_distance = '+0.75'
        elif vals.get('od_sph_distance') == '+0.50':
            od_sph_distance = '+0.50'
        elif vals.get('od_sph_distance') == '+0.25':
            od_sph_distance = '+0.25'
        elif vals.get('od_sph_distance') == '+0.00':
            od_sph_distance = '+0.00'

        elif vals.get('od_sph_distance') == '+1.75':
            od_sph_distance = '+1.75'
        elif vals.get('od_sph_distance') == '+1.50':
            od_sph_distance = '+1.50'
        elif vals.get('od_sph_distance') == '+1.25':
            od_sph_distance = '+1.25'
        elif vals.get('od_sph_distance') == '+1.00':
            od_sph_distance = '+1.00'

        elif vals.get('od_sph_distance') == '+2.75':
            od_sph_distance = '+2.75'
        elif vals.get('od_sph_distance') == '+2.50':
            od_sph_distance = '+2.50'
        elif vals.get('od_sph_distance') == '+2.25':
            od_sph_distance = '+2.25'
        elif vals.get('od_sph_distance') == '+2.00':
            od_sph_distance = '+2.00'

        elif vals.get('od_sph_distance') == '+3.75':
            od_sph_distance = '+3.75'
        elif vals.get('od_sph_distance') == '+3.50':
            od_sph_distance = '+3.50'
        elif vals.get('od_sph_distance') == '+3.25':
            od_sph_distance = '+3.25'
        elif vals.get('od_sph_distance') == '+3.00':
            od_sph_distance = '+3.00'

        elif vals.get('od_sph_distance') == '+4.75':
            od_sph_distance = '+4.75'
        elif vals.get('od_sph_distance') == '+4.50':
            od_sph_distance = '+4.50'
        elif vals.get('od_sph_distance') == '+4.25':
            od_sph_distance = '+4.25'
        elif vals.get('od_sph_distance') == '+4.00':
            od_sph_distance = '+4.00'

        elif vals.get('od_sph_distance') == '+5.75':
            od_sph_distance = '+5.75'
        elif vals.get('od_sph_distance') == '+5.50':
            od_sph_distance = '+5.50'
        elif vals.get('od_sph_distance') == '+5.25':
            od_sph_distance = '+5.25'
        elif vals.get('od_sph_distance') == '+5.00':
            od_sph_distance = '+5.00'

        elif vals.get('od_sph_distance') == '+6.75':
            od_sph_distance = '+6.75'
        elif vals.get('od_sph_distance') == '+6.50':
            od_sph_distance = '+6.50'
        elif vals.get('od_sph_distance') == '+6.25':
            od_sph_distance = '+6.25'
        elif vals.get('od_sph_distance') == '+6.00':
            od_sph_distance = '+6.00'

        elif vals.get('od_sph_distance') == '+7.75':
            od_sph_distance = '+7.75'
        elif vals.get('od_sph_distance') == '+7.50':
            od_sph_distance = '+7.50'
        elif vals.get('od_sph_distance') == '+7.25':
            od_sph_distance = '+7.25'
        elif vals.get('od_sph_distance') == '+7.00':
            od_sph_distance = '+7.00'

        elif vals.get('od_sph_distance') == '+8.75':
            od_sph_distance = '+8.75'
        elif vals.get('od_sph_distance') == '+8.50':
            od_sph_distance = '+8.50'
        elif vals.get('od_sph_distance') == '+8.25':
            od_sph_distance = '+8.25'
        elif vals.get('od_sph_distance') == '+8.00':
            od_sph_distance = '+8.00'

        elif vals.get('od_sph_distance') == '+9.75':
            od_sph_distance = '+9.75'
        elif vals.get('od_sph_distance') == '+9.50':
            od_sph_distance = '+9.50'
        elif vals.get('od_sph_distance') == '+9.25':
            od_sph_distance = '+9.25'
        elif vals.get('od_sph_distance') == '+9.00':
            od_sph_distance = '+9.00'

        elif vals.get('od_sph_distance') == '+10.75':
            od_sph_distance = '+10.75'
        elif vals.get('od_sph_distance') == '+10.50':
            od_sph_distance = '+10.50'
        elif vals.get('od_sph_distance') == '+10.25':
            od_sph_distance = '+10.25'
        elif vals.get('od_sph_distance') == '+10.00':
            od_sph_distance = '+10.00'

        elif vals.get('od_sph_distance') == '+11.75':
            od_sph_distance = '+11.75'
        elif vals.get('od_sph_distance') == '+11.50':
            od_sph_distance = '+11.50'
        elif vals.get('od_sph_distance') == '+11.25':
            od_sph_distance = '+11.25'
        elif vals.get('od_sph_distance') == '+11.00':
            od_sph_distance = '+11.00'

        elif vals.get('od_sph_distance') == '+12.00':
            od_sph_distance = '+12.00'

        od_cyl_distance = None
        if vals.get('od_cyl_distance') == '0.00':
            od_cyl_distance = '0.00'
        elif vals.get('od_cyl_distance') == '-6.00':
            od_cyl_distance = '-6.00'
        elif vals.get('od_cyl_distance') == '-5.75':
            od_cyl_distance = '-6.00'
        elif vals.get('od_cyl_distance') == '-5.50':
            od_cyl_distance = '-6.00'

        od_axis_distance = None
        if vals.get('od_axis_distance') == '1':
            od_axis_distance = '1'
        elif vals.get('od_axis_distance') == '2':
            od_axis_distance = '2'
        elif vals.get('od_axis_distance') == '3':
            od_axis_distance = '3'
        elif vals.get('od_axis_distance') == '4':
            od_axis_distance = '4'
        elif vals.get('od_axis_distance') == '5':
            od_axis_distance = '5'

        od_add_distance = None
        if vals.get('od_add_distance') == '0.00':
            od_add_distance = '0.00'
        elif vals.get('od_add_distance') == '+0.25':
            od_add_distance = '+0.25'
        elif vals.get('od_add_distance') == '+0.50':
             od_add_distance= '+0.50'
        elif vals.get('od_add_distance') == '+0.75':
             od_add_distance= '+0.75'
        elif vals.get('od_add_distance') == '+1.00':
             od_add_distance= '+1.00'
        elif vals.get('od_add_distance') == '+1.25':
            od_add_distance= '+1.25'
        elif vals.get('od_add_distance') == '+1.50':
            od_add_distance= '+1.50'
        elif vals.get('od_add_distance') == '+1.75':
            od_add_distance= '+1.75'
        elif vals.get('od_add_distance') == '+2.00':
             od_add_distance= '+2.00'
        elif vals.get('od_add_distance') == '+2.25':
             od_add_distance= '+2.25'
        elif vals.get('od_add_distance') == '+2.50':
             od_add_distance= '+2.50'
        elif vals.get('od_add_distance') == '+2.75':
            od_add_distance= '+2.75'
        elif vals.get('od_add_distance') == '3.00':
            od_add_distance= '3.00'
        elif vals.get('od_add_distance') == '+3.25':
            od_add_distance = '+3.25'
        elif vals.get('od_add_distance') == '+3.50':
             od_add_distance= '+3.50'

        od_prism_distance = None
        if vals.get('od_prism_distance') == '0.25':
            od_prism_distance = '0.25'
        elif vals.get('od_prism_distance') == '0.50':
            od_prism_distance = '0.50'

        od_base_distance = None
        if vals.get('od_base_distance') == 'IN':
            od_base_distance = 'IN'
        elif vals.get('od_base_distance') == 'Select':
            od_base_distance = 'Select'
        elif vals.get('od_base_distance') == 'OUT':
            od_base_distance = 'OUT'
        elif vals.get('od_base_distance') == 'UP':
            od_base_distance = 'UP'
        elif vals.get('od_base_distance') == 'DOWN':
            od_base_distance = 'DOWN'
        """         ------------------------------------------------------------------------------------------ """
        os_sph_distance = None
        if vals.get('os_sph_distance') == '0.00':
            os_sph_distance = '0.00'
        elif vals.get('os_sph_distance') == '-16.00':
            os_sph_distance = '-16.00'

        elif vals.get('os_sph_distance') == '-15.75':
            os_sph_distance = '-15.75'
        elif vals.get('os_sph_distance') == '15.50':
            os_sph_distance = '15.50'
        elif vals.get('os_sph_distance') == '-15.25':
            os_sph_distance = '-15.25'
        elif vals.get('os_sph_distance') == '-15.00':
            os_sph_distance = '-15.00'

        elif vals.get('os_sph_distance') == '-14.75':
            os_sph_distance = '-14.75'
        elif vals.get('os_sph_distance') == '14.50':
            os_sph_distance = '14.50'
        elif vals.get('os_sph_distance') == '-14.25':
            os_sph_distance = '-14.25'
        elif vals.get('os_sph_distance') == '-14.00':
            os_sph_distance = '-14.00'

        elif vals.get('os_sph_distance') == '-13.75':
            os_sph_distance = '-13.75'
        elif vals.get('os_sph_distance') == '13.50':
            os_sph_distance = '13.50'
        elif vals.get('os_sph_distance') == '-13.25':
            os_sph_distance = '-13.25'
        elif vals.get('os_sph_distance') == '-13.00':
            os_sph_distance = '-13.00'

        elif vals.get('os_sph_distance') == '-12.75':
            os_sph_distance = '-12.75'
        elif vals.get('os_sph_distance') == '12.50':
            os_sph_distance = '12.50'
        elif vals.get('os_sph_distance') == '-12.25':
            os_sph_distance = '-12.25'
        elif vals.get('os_sph_distance') == '-12.00':
            os_sph_distance = '-12.00'

        elif vals.get('os_sph_distance') == '-11.75':
            os_sph_distance = '-11.75'
        elif vals.get('os_sph_distance') == '11.50':
            os_sph_distance = '11.50'
        elif vals.get('os_sph_distance') == '-11.25':
            os_sph_distance = '-11.25'
        elif vals.get('os_sph_distance') == '-11.00':
            os_sph_distance = '-11.00'

        elif vals.get('os_sph_distance') == '-10.75':
            od_sph_distance = '-10.75'
        elif vals.get('os_sph_distance') == '-10.50':
            os_sph_distance = '-10.50'
        elif vals.get('os_sph_distance') == '-10.25':
            os_sph_distance = '-10.25'
        elif vals.get('os_sph_distance') == '-10.00':
            os_sph_distance = '-10.00'

        elif vals.get('os_sph_distance') == '-9.75':
            os_sph_distance = '-9.75'
        elif vals.get('os_sph_distance') == '-9.50':
            os_sph_distance = '-9.50'
        elif vals.get('os_sph_distance') == '-9.25':
            os_sph_distance = '-9.25'
        elif vals.get('os_sph_distance') == '-9.00':
            os_sph_distance = '-9.00'

        elif vals.get('os_sph_distance') == '-8.75':
            os_sph_distance = '-8.75'
        elif vals.get('os_sph_distance') == '-8.50':
            os_sph_distance = '-8.50'
        elif vals.get('os_sph_distance') == '-8.25':
            os_sph_distance = '-8.25'
        elif vals.get('os_sph_distance') == '-8.00':
            os_sph_distance = '-8.00'

        elif vals.get('os_sph_distance') == '-7.75':
            os_sph_distance = '-7.75'
        elif vals.get('os_sph_distance') == '-7.50':
            os_sph_distance = '-7.50'
        elif vals.get('os_sph_distance') == '-7.25':
            os_sph_distance = '-7.25'
        elif vals.get('os_sph_distance') == '-7.00':
            os_sph_distance = '-7.00'

        elif vals.get('os_sph_distance') == '-6.75':
            os_sph_distance = '-6.75'
        elif vals.get('os_sph_distance') == '-6.50':
            os_sph_distance = '-6.50'
        elif vals.get('os_sph_distance') == '-6.25':
            os_sph_distance = '-6.25'
        elif vals.get('os_sph_distance') == '-6.00':
            os_sph_distance = '-6.00'

        elif vals.get('os_sph_distance') == '-5.75':
            os_sph_distance = '-5.75'
        elif vals.get('os_sph_distance') == '-5.50':
            os_sph_distance = '-5.50'
        elif vals.get('os_sph_distance') == '-5.25':
            os_sph_distance = '-5.25'
        elif vals.get('os_sph_distance') == '-5.00':
            os_sph_distance = '-5.00'

        elif vals.get('os_sph_distance') == '-4.75':
            os_sph_distance = '-4.75'
        elif vals.get('os_sph_distance') == '-4.50':
            os_sph_distance = '-4.50'
        elif vals.get('os_sph_distance') == '-4.25':
            os_sph_distance = '-4.25'
        elif vals.get('os_sph_distance') == '-4.00':
            os_sph_distance = '-4.00'

        elif vals.get('os_sph_distance') == '-3.75':
            os_sph_distance = '-3.75'
        elif vals.get('os_sph_distance') == '-3.50':
            os_sph_distance = '-3.50'
        elif vals.get('os_sph_distance') == '-3.25':
            os_sph_distance = '-3.25'
        elif vals.get('os_sph_distance') == '-3.00':
            os_sph_distance= '-3.00'

        elif vals.get('os_sph_distance') == '-2.75':
            os_sph_distance = '-2.75'
        elif vals.get('os_sph_distance') == '-2.50':
            os_sph_distance = '-2.50'
        elif vals.get('os_sph_distance') == '-2.25':
            os_sph_distance = '-2.25'
        elif vals.get('os_sph_distance') == '-2.00':
            os_sph_distance = '-2.00'

        elif vals.get('os_sph_distance') == '-1.75':
            os_sph_distance = '-1.75'
        elif vals.get('os_sph_distance') == '-1.50':
            os_sph_distance = '-1.50'
        elif vals.get('os_sph_distance') == '-1.25':
            os_sph_distance = '-1.25'
        elif vals.get('os_sph_distance') == '-1.00':
            os_sph_distance = '-1.00'

        elif vals.get('os_sph_distance') == '-0.75':
           os_sph_distance = '-0.75'
        elif vals.get('os_sph_distance') == '-0.50':
            os_sph_distance = '-0.50'
        elif vals.get('os_sph_distance') == '-0.25':
            os_sph_distance = '-0.25'
        elif vals.get('os_sph_distance') == '-0.00':
            os_sph_distance = '-0.00'

        elif vals.get('od_sph_distance') == '+0.75':
            od_sph_distance = '+0.75'
        elif vals.get('od_sph_distance') == '+0.50':
            od_sph_distance = '+0.50'
        elif vals.get('od_sph_distance') == '+0.25':
            od_sph_distance = '+0.25'
        elif vals.get('od_sph_distance') == '+0.00':
            od_sph_distance = '+0.00'

        elif vals.get('od_sph_distance') == '+1.75':
            od_sph_distance = '+1.75'
        elif vals.get('od_sph_distance') == '+1.50':
            od_sph_distance = '+1.50'
        elif vals.get('od_sph_distance') == '+1.25':
            od_sph_distance = '+1.25'
        elif vals.get('od_sph_distance') == '+1.00':
            od_sph_distance = '+1.00'

        elif vals.get('od_sph_distance') == '+2.75':
            od_sph_distance = '+2.75'
        elif vals.get('od_sph_distance') == '+2.50':
            od_sph_distance = '+2.50'
        elif vals.get('os_sph_distance') == '+2.25':
            os_sph_distance = '+2.25'
        elif vals.get('os_sph_distance') == '+2.00':
            os_sph_distance = '+2.00'

        elif vals.get('os_sph_distance') == '+3.75':
            os_sph_distance = '+3.75'
        elif vals.get('os_sph_distance') == '+3.50':
            os_sph_distance = '+3.50'
        elif vals.get('os_sph_distance') == '+3.25':
            os_sph_distance = '+3.25'
        elif vals.get('os_sph_distance') == '+3.00':
            os_sph_distance = '+3.00'

        elif vals.get('os_sph_distance') == '+4.75':
            os_sph_distance = '+4.75'
        elif vals.get('os_sph_distance') == '+4.50':
            os_sph_distance = '+4.50'
        elif vals.get('os_sph_distance') == '+4.25':
            os_sph_distance = '+4.25'
        elif vals.get('os_sph_distance') == '+4.00':
            os_sph_distance = '+4.00'

        elif vals.get('od_sph_distance') == '+5.75':
            od_sph_distance = '+5.75'
        elif vals.get('od_sph_distance') == '+5.50':
            od_sph_distance = '+5.50'
        elif vals.get('od_sph_distance') == '+5.25':
            od_sph_distance = '+5.25'
        elif vals.get('od_sph_distance') == '+5.00':
            od_sph_distance = '+5.00'

        elif vals.get('od_sph_distance') == '+6.75':
            od_sph_distance = '+6.75'
        elif vals.get('od_sph_distance') == '+6.50':
            od_sph_distance = '+6.50'
        elif vals.get('od_sph_distance') == '+6.25':
            od_sph_distance = '+6.25'
        elif vals.get('od_sph_distance') == '+6.00':
            od_sph_distance = '+6.00'

        elif vals.get('os_sph_distance') == '+7.75':
            os_sph_distance = '+7.75'
        elif vals.get('os_sph_distance') == '+7.50':
            os_sph_distance = '+7.50'
        elif vals.get('os_sph_distance') == '+7.25':
            os_sph_distance = '+7.25'
        elif vals.get('os_sph_distance') == '+7.00':
            os_sph_distance = '+7.00'

        elif vals.get('os_sph_distance') == '+8.75':
            os_sph_distance = '+8.75'
        elif vals.get('os_sph_distance') == '+8.50':
            os_sph_distance = '+8.50'
        elif vals.get('os_sph_distance') == '+8.25':
            os_sph_distance = '+8.25'
        elif vals.get('os_sph_distance') == '+8.00':
            os_sph_distance = '+8.00'

        elif vals.get('os_sph_distance') == '+9.75':
            os_sph_distance = '+9.75'
        elif vals.get('os_sph_distance') == '+9.50':
            os_sph_distance = '+9.50'
        elif vals.get('os_sph_distance') == '+9.25':
            os_sph_distance = '+9.25'
        elif vals.get('os_sph_distance') == '+9.00':
            os_sph_distance = '+9.00'

        elif vals.get('os_sph_distance') == '+10.75':
            os_sph_distance = '+10.75'
        elif vals.get('os_sph_distance') == '+10.50':
            os_sph_distance = '+10.50'
        elif vals.get('os_sph_distance') == '+10.25':
            os_sph_distance = '+10.25'
        elif vals.get('os_sph_distance') == '+10.00':
            os_sph_distance = '+10.00'

        elif vals.get('os_sph_distance') == '+11.75':
            os_sph_distance = '+11.75'
        elif vals.get('os_sph_distance') == '+11.50':
            os_sph_distance = '+11.50'
        elif vals.get('os_sph_distance') == '+11.25':
            os_sph_distance = '+11.25'
        elif vals.get('os_sph_distance') == '+11.00':
            os_sph_distance = '+11.00'

        elif vals.get('os_sph_distance') == '+12.00':
            os_sph_distance = '+12.00'

        os_cyl_distance = None
        if vals.get('os_cyl_distance') == '-3.50':
            os_cyl_distance = '-3.50'
        elif vals.get('os_cyl_distance') == '-3.25':
            os_cyl_distance = '-3.25'

        os_ax_distance = None
        if vals.get('os_ax_distance') == '1':
            os_ax_distance = '1'
        elif vals.get('os_ax_distance') == '2':
            os_ax_distance = '2'

        os_add_distance = None
        if vals.get('os_add_distance') == '0.00':
            os_add_distance = '0.00'
        elif vals.get('os_add_distance') == '+0.25':
            os_add_distance = '+0.25'
        elif vals.get('os_add_distance') == '+0.50':
             os_add_distance= '+0.50'
        elif vals.get('os_add_distance') == '+0.75':
             os_add_distance= '+0.75'
        elif vals.get('os_add_distance') == '+1.00':
             os_add_distance= '+1.00'
        elif vals.get('os_add_distance') == '+1.25':
            os_add_distance= '+1.25'
        elif vals.get('os_add_distance') == '+1.50':
            os_add_distance= '+1.50'
        elif vals.get('os_add_distance') == '+1.75':
            os_add_distance= '+1.75'
        elif vals.get('os_add_distance') == '+2.00':
             os_add_distance= '+2.00'
        elif vals.get('os_add_distance') == '+2.25':
             os_add_distance= '+2.25'
        elif vals.get('os_add_distance') == '+2.50':
             os_add_distance= '+2.50'
        elif vals.get('os_add_distance') == '+2.75':
            os_add_distance= '+2.75'
        elif vals.get('os_add_distance') == '3.00':
            os_add_distance = '3.00'
        elif vals.get('os_add_distance') == '+3.25':
            os_add_distance= '+3.25'
        elif vals.get('os_add_distance') == '+3.50':
             os_add_distance= '+3.50'






        os_prism_distance = None
        if vals.get('os_prism_distance') == '0.25':
            os_prism_distance = '0.25'
        elif vals.get('os_prism_distance') == '0.50':
            os_prism_distance = '0.50'

        os_base_distance = None
        if vals.get('os_base_distance') == 'IN':
            os_base_distance = 'IN'
        elif vals.get('os_base_distance') == 'Select':
            os_base_distance = 'Select'
        elif vals.get('os_base_distance') == 'OUT':
            os_base_distance = 'OUT'
        elif vals.get('os_base_distance') == 'UP':
            os_base_distance = 'UP'
        elif vals.get('os_base_distance') == 'DOWN':
            os_base_distance = 'DOWN'
        """         ------------------------------------------------------------------------------------------ """
        od_sph_near = None
        if vals.get('od_sph_near') == '-8.00':
            od_sph_near = '-8.00'
        elif vals.get('od_sph_near') == '-7.75':
            od_sph_near = '-7.75'
        elif vals.get('od_sph_near') =='-7.50':
            od_sph_near='-7.50'
        elif vals.get('od_sph_near') =='-7.25':
            od_sph_near='-7.25'
        elif vals.get('od_sph_near') =='-7.00':
            od_sph_near='-7.00'
        elif vals.get('od_sph_near') =='-6.75':
            od_sph_near='-6.75'
        elif vals.get('od_sph_near') =='-6.50':
            od_sph_near='-6.50'
        elif vals.get('od_sph_near') =='-6.25':
            od_sph_near='-6.25'
        elif vals.get('od_sph_near') =='-6.00':
            od_sph_near='-6.00'
        elif vals.get('od_sph_near') =='-5.75':
            od_sph_near='-5.75'
        elif vals.get('od_sph_near') =='-5.50':
            od_sph_near='-5.50'
        elif vals.get('od_sph_near') =='-5.25':
            od_sph_near='-5.25'
        elif vals.get('od_sph_near') =='-5.00':
            od_sph_near='-5.00'
        elif vals.get('od_sph_near') =='-4.75':
            od_sph_near='-4.75'
        elif vals.get('od_sph_near') =='-4.50':
            od_sph_near='-4.50'
        elif vals.get('od_sph_near') =='-4.25':
            od_sph_near='-4.25'
        elif vals.get('od_sph_near') =='-4.00':
            od_sph_near='-4.00'
        elif vals.get('od_sph_near') =='-3.75':
            od_sph_near='-3.75'
        elif vals.get('od_sph_near') =='-3.50':
            od_sph_near='-3.50'
        elif vals.get('od_sph_near') =='-3.25':
            od_sph_near='-3.25'
        elif vals.get('od_sph_near') =='-3.00':
            od_sph_near='-3.00'
        elif vals.get('od_sph_near') =='-2.75':
            od_sph_near='-2.75'
        elif vals.get('od_sph_near') =='-2.50':
            od_sph_near='-2.50'
        elif vals.get('od_sph_near') =='-2.25':
            od_sph_near='-2.25'
        elif vals.get('od_sph_near') =='-2.00':
            od_sph_near='-2.00'
        elif vals.get('od_sph_near') =='-1.75':
            od_sph_near='-1.75'
        elif vals.get('od_sph_near') =='-1.50':
            od_sph_near='-1.50'
        elif vals.get('od_sph_near') =='-1.25':
            od_sph_near='-1.25'
        elif vals.get('od_sph_near') =='-1.00':
            od_sph_near='-1.00'
        elif vals.get('od_sph_near') =='0.75':
            od_sph_near='0.75'
        elif vals.get('od_sph_near') =='-0.50':
            od_sph_near='-0.50'
        elif vals.get('od_sph_near') =='-0.25':
            od_sph_near='-0.25'
        elif vals.get('od_sph_near') =='-0.00':
            od_sph_near='-0.00'
        elif vals.get('od_sph_near') =='+0.25':
            od_sph_near='+0.25'
        elif vals.get('od_sph_near') =='+0.50':
            od_sph_near='+0.50'
        elif vals.get('od_sph_near') =='+0.75':
            od_sph_near='+0.75'
        elif vals.get('od_sph_near') =='+1.00':
            od_sph_near='+1.00'
        elif vals.get('od_sph_near') =='+1.25':
            od_sph_near='+1.25'
        elif vals.get('od_sph_near') =='+1.50':
            od_sph_near='+1.25'
        elif vals.get('od_sph_near') =='+1.75':
            od_sph_near='+1.75'
        elif vals.get('od_sph_near') =='+2.00':
            od_sph_near='+2.00'
        elif vals.get('od_sph_near') =='+2.25':
            od_sph_near='+2.25'
        elif vals.get('od_sph_near') =='+2.50':
            od_sph_near='+2.50'
        elif vals.get('od_sph_near') =='+2.75':
            od_sph_near='+2.75'
        elif vals.get('od_sph_near') =='+3.00':
            od_sph_near='+3.00'
        elif vals.get('od_sph_near') =='+3.25':
            od_sph_near='+3.25'
        elif vals.get('od_sph_near') =='+3.50':
            od_sph_near='+3.50'
        elif vals.get('od_sph_near') =='+3.75':
            od_sph_near='+3.75'
        elif vals.get('od_sph_near') =='+4.00':
            od_sph_near='+4.00'
        elif vals.get('od_sph_near') =='+4.25':
            od_sph_near='+4.25'
        elif vals.get('od_sph_near') =='+4.50':
            od_sph_near='+4.50'
        elif vals.get('od_sph_near') =='+4.75':
            od_sph_near='+4.75'
        elif vals.get('od_sph_near') =='+5.00':
            od_sph_near='+5.00'
        elif vals.get('od_sph_near') =='+5.25':
            od_sph_near='+5.25'
        elif vals.get('od_sph_near') =='+5.50':
            od_sph_near='+5.50'
        elif vals.get('od_sph_near') =='+5.75':
            od_sph_near='+5.75'
        elif vals.get('od_sph_near') =='+6.00':
            od_sph_near='+6.00'
        elif vals.get('od_sph_near') =='+6.25':
            od_sph_near='+6.25'
        elif vals.get('od_sph_near') =='+6.50':
            od_sph_near='+6.50'
        elif vals.get('od_sph_near') =='+6.75':
            od_sph_near='+6.75'
        elif vals.get('od_sph_near') =='6.00':
            od_sph_near='6.00'


        od_cyl_near = None
        if vals.get('od_cyl_near') == '-3.50':
            od_cyl_near = '-3.50'
        elif vals.get('od_cyl_near') == '-3.25':
            od_cyl_near = '-3.25'

        od_ax_near = None
        if vals.get('od_ax_near') == '1':
            od_ax_near = '1'
        elif vals.get('od_ax_near') == '2':
            od_ax_near = '2'

        od_add_near = None
        if vals.get('od_add_near') == '0.00':
            od_add_near = '0.00'
        elif vals.get('od_add_near') == '+0.25':
            od_add_near = '+0.25'
        elif vals.get('od_add_near') == '+0.50':
             od_add_near= '+0.50'
        elif vals.get('od_add_near') == '+0.75':
             od_add_near= '+0.75'
        elif vals.get('od_add_near') == '+1.00':
             od_add_near= '+1.00'
        elif vals.get('od_add_near') == '+1.25':
            od_add_near= '+1.25'
        elif vals.get('od_add_near') == '+1.50':
            od_add_near= '+1.50'
        elif vals.get('od_add_near') == '+1.75':
            od_add_near= '+1.75'
        elif vals.get('od_add_near') == '+2.00':
             od_add_near= '+2.00'
        elif vals.get('od_add_near') == '+2.25':
             od_add_near= '+2.25'
        elif vals.get('od_add_near') == '+2.50':
             od_add_near= '+2.50'
        elif vals.get('od_add_near') == '+2.75':
            od_add_near= '+2.75'
        elif vals.get('od_add_near') == '3.00':
            od_add_near= '3.00'
        elif vals.get('od_add_near') == '+3.25':
            od_add_near= '+3.25'
        elif vals.get('od_add_near') == '+3.50':
             od_add_near= '+3.50'

        od_prism_near = None
        if vals.get('od_prism_near') == '0.25':
            od_prism_near = '0.25'
        elif vals.get('od_prism_near') == '0.50':
            od_prism_near = '0.50'

        od_base_near = None
        if vals.get('od_base_near') == 'IN':
            od_base_near = 'IN'
        elif vals.get('od_base_near') == 'Select':
            od_base_near = 'Select'
        elif vals.get('od_base_near') == 'OUT':
            od_base_near = 'OUT'
        elif vals.get('od_base_near') == 'UP':
            od_base_near = 'UP'
        elif vals.get('od_base_near') == 'DOWN':
            od_base_near = 'DOWN'
        """         ------------------------------------------------------------------------------------------ """
        os_sph_near = None
        if vals.get('os_sph_near') == '-8.00':
            os_sph_near = '-8.00'
        elif vals.get('os_sph_near') == '-7.75':
            os_sph_near = '-7.75'
        elif vals.get('os_sph_near') =='-7.50':
            os_sph_near='-7.50'
        elif vals.get('os_sph_near') =='-7.25':
            os_sph_near='-7.25'
        elif vals.get('os_sph_near') =='-7.00':
            os_sph_near='-7.00'
        elif vals.get('os_sph_near') =='-6.75':
            os_sph_near='-6.75'
        elif vals.get('os_sph_near') =='-6.50':
            os_sph_near='-6.50'
        elif vals.get('os_sph_near') =='-6.25':
            os_sph_near='-6.25'
        elif vals.get('os_sph_near') =='-6.00':
            os_sph_near='-6.00'
        elif vals.get('os_sph_near') =='-5.75':
            os_sph_near='-5.75'
        elif vals.get('os_sph_near') =='-5.50':
            os_sph_near='-5.50'
        elif vals.get('os_sph_near') =='-5.25':
            os_sph_near='-5.25'
        elif vals.get('os_sph_near') =='-5.00':
            os_sph_near='-5.00'
        elif vals.get('os_sph_near') =='-4.75':
            os_sph_near='-4.75'
        elif vals.get('os_sph_near') =='-4.50':
            os_sph_near='-4.50'
        elif vals.get('os_sph_near') =='-4.25':
            os_sph_near='-4.25'
        elif vals.get('os_sph_near') =='-4.00':
            os_sph_near='-4.00'
        elif vals.get('os_sph_near') =='-3.75':
            os_sph_near='-3.75'
        elif vals.get('os_sph_near') =='-3.50':
            os_sph_near='-3.50'
        elif vals.get('os_sph_near') =='-3.25':
            os_sph_near='-3.25'
        elif vals.get('os_sph_near') =='-3.00':
            os_sph_near='-3.00'
        elif vals.get('os_sph_near') =='-2.75':
            os_sph_near='-2.75'
        elif vals.get('os_sph_near') =='-2.50':
            os_sph_near='-2.50'
        elif vals.get('os_sph_near') =='-2.25':
            os_sph_near='-2.25'
        elif vals.get('os_sph_near') =='-2.00':
            os_sph_near='-2.00'
        elif vals.get('os_sph_near') =='-1.75':
            os_sph_near='-1.75'
        elif vals.get('os_sph_near') =='-1.50':
            os_sph_near='-1.50'
        elif vals.get('os_sph_near') =='-1.25':
            os_sph_near='-1.25'
        elif vals.get('os_sph_near') =='-1.00':
            os_sph_near='-1.00'
        elif vals.get('os_sph_near') =='0.75':
            os_sph_near='0.75'
        elif vals.get('os_sph_near') =='-0.50':
            os_sph_near='-0.50'
        elif vals.get('os_sph_near') =='-0.25':
            os_sph_near='-0.25'
        elif vals.get('os_sph_near') =='-0.00':
            os_sph_near='-0.00'
        elif vals.get('os_sph_near') =='+0.25':
            os_sph_near='+0.25'
        elif vals.get('os_sph_near') =='+0.50':
            os_sph_near='+0.50'
        elif vals.get('os_sph_near') =='+0.75':
            os_sph_near='+0.75'
        elif vals.get('os_sph_near') =='+1.00':
            os_sph_near='+1.00'
        elif vals.get('os_sph_near') =='+1.25':
            os_sph_near='+1.25'
        elif vals.get('os_sph_near') =='+1.50':
            os_sph_near='+1.25'
        elif vals.get('os_sph_near') =='+1.75':
            os_sph_near='+1.75'
        elif vals.get('os_sph_near') =='+2.00':
            os_sph_near='+2.00'
        elif vals.get('os_sph_near') =='+2.25':
            os_sph_near='+2.25'
        elif vals.get('os_sph_near') =='+2.50':
            os_sph_near='+2.50'
        elif vals.get('os_sph_near') =='+2.75':
            os_sph_near='+2.75'
        elif vals.get('os_sph_near') =='+3.00':
            os_sph_near='+3.00'
        elif vals.get('os_sph_near') =='+3.25':
            os_sph_near='+3.25'
        elif vals.get('os_sph_near') =='+3.50':
            os_sph_near='+3.50'
        elif vals.get('os_sph_near') =='+3.75':
            os_sph_near='+3.75'
        elif vals.get('os_sph_near') =='+4.00':
            os_sph_near='+4.00'
        elif vals.get('os_sph_near') =='+4.25':
            os_sph_near='+4.25'
        elif vals.get('os_sph_near') =='+4.50':
            os_sph_near='+4.50'
        elif vals.get('os_sph_near') =='+4.75':
            os_sph_near='+4.75'
        elif vals.get('os_sph_near') =='+5.00':
            os_sph_near='+5.00'
        elif vals.get('os_sph_near') =='+5.25':
            os_sph_near='+5.25'
        elif vals.get('os_sph_near') =='+5.50':
            os_sph_near='+5.50'
        elif vals.get('os_sph_near') =='+5.75':
            os_sph_near='+5.75'
        elif vals.get('os_sph_near') =='+6.00':
            os_sph_near='+6.00'
        elif vals.get('os_sph_near') =='+6.25':
            os_sph_near='+6.25'
        elif vals.get('os_sph_near') =='+6.50':
            os_sph_near='+6.50'
        elif vals.get('os_sph_near') =='+6.75':
            os_sph_near='+6.75'
        elif vals.get('os_sph_near') =='6.00':
            os_sph_near='6.00'

        os_cyl_near = None
        if vals.get('os_cyl_near') == '-3.50':
            os_cyl_near = '-3.50'
        elif vals.get('os_cyl_near') == '-3.25':
            os_cyl_near = '-3.25'

        os_ax_near = None
        if vals.get('os_ax_near') == '1':
            os_ax_near = '1'
        elif vals.get('os_ax_near') == '2':
            os_ax_near = '2'

        os_add_near = None
        if vals.get('os_add_near') == '0.00':
            os_add_near = '0.00'
        elif vals.get('os_add_near') == '+0.25':
            os_add_near = '+0.25'

        elif vals.get('os_add_near') == '+0.50':
             os_add_near= '+0.50'
        elif vals.get('os_add_near') == '+0.75':
             os_add_near= '+0.75'
        elif vals.get('os_add_near') == '+1.00':
             os_add_near= '+1.00'
        elif vals.get('os_add_near') == '+1.25':
            os_add_near= '+1.25'
        elif vals.get('os_add_near') == '+1.50':
            os_add_near= '+1.50'
        elif vals.get('os_add_near') == '+1.75':
            os_add_near= '+1.75'
        elif vals.get('os_add_near') == '+2.00':
             os_add_near= '+2.00'
        elif vals.get('os_add_near') == '+2.25':
             os_add_near= '+2.25'
        elif vals.get('os_add_near') == '+2.50':
             os_add_near= '+2.50'
        elif vals.get('os_add_near') == '+2.75':
            os_add_near= '+2.75'
        elif vals.get('os_add_near') == '3.00':
            os_add_near= '3.00'
        elif vals.get('os_add_near') == '+3.25':
            os_add_near= '+3.25'
        elif vals.get('os_add_near') == '+3.50':
             os_add_near= '+3.50'

        os_prism_near = None
        if vals.get('os_prism_near') == '0.25':
            os_prism_near = '0.25'
        elif vals.get('os_prism_near') == '0.50':
            os_prism_near = '0.50'

        os_base_near = None

        if vals.get('os_base_near') == 'IN':
            os_base_near = 'IN'
        elif vals.get('os_base_near') == 'Select':
            os_base_near = 'Select'
        elif vals.get('os_base_near') == 'OUT':
            os_base_near = 'OUT'
        elif vals.get('os_base_near') == 'UP':
            os_base_near = 'UP'
        elif vals.get('os_base_near') == 'DOWN':
            os_base_near = 'DOWN'
        """         ------------------------------------------------------------------------------------------ """




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
            'os_cyl_distance': os_cyl_distance if os_cyl_distance else '',
            'os_ax_distance': os_ax_distance if os_ax_distance else '',
            'os_add_distance': os_add_distance if os_add_distance else '',
            'os_prism_distance':os_prism_distance if  os_prism_distance else '',
            'os_base_distance':  os_base_distance if  os_base_distance else '',
            'od_sph_near': od_sph_near if od_sph_near else '',
            'od_cyl_near': od_cyl_near if od_cyl_near else '',
            'od_ax_near': od_ax_near if od_ax_near else '',
            'od_add_near': od_add_near if od_add_near else '',
            'od_prism_near': od_prism_near if od_prism_near else '',
            'od_base_near': od_base_near if od_base_near else '',
            'os_sph_near': os_sph_near if os_sph_near else '',
            'os_cyl_near': os_cyl_near if os_cyl_near else '',
            'os_ax_near': os_ax_near if os_ax_near else '',
            'os_add_near': os_add_near if os_add_near else '',
            'os_prism_near': os_prism_near if os_prism_near else '',
            'os_base_near': os_base_near if os_base_near else '',
            'state': 'Confirm',
            # '': od_sph_distance if od_sph_distance else '',

        }
        print(new_vals)
        rec = self.env['dr.prescription'].create(new_vals)
        new_vals = {'id': rec.id if rec.id else '',
                         'dr': [rec.dr.id, rec.dr.name] if rec.dr else [],
                         'customer': [rec.customer.id, rec.customer.name] if rec.customer else [],
                         'test_type': [rec.test_type.id, rec.test_type.name] if rec.test_type else [],
                         'checkup_date': rec.checkup_date if rec.checkup_date else '',
                         'prescription_type': rec.prescription_type if rec.prescription_type else '',
                         'od_sph_distance': rec.od_sph_distance if rec.od_sph_distance else '',
                         'name': rec.name if rec.name else '',
                         'state': rec.state if rec.state else '',
                         }

        return new_vals
