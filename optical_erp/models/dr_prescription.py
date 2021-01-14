from odoo import api, fields, models,_
from odoo.tools import datetime


class DrPrescription(models.Model):
    _name ='dr.prescription'
    _description = 'Doctor Prescription'
    _rec_name = 'name'




    dr = fields.Many2one('optical.dr',string='Optometrist',readonly=True)
    customer = fields.Many2one('res.partner',domain=[('customer_rank','=','1')],string='Customer',readonly=False)
    customer_age = fields.Integer(related='customer.age')
    checkup_date = fields.Date('Checkup Date',default=fields.Datetime.now())
    test_type = fields.Many2one('eye.test.type')


    def default_eye_examination_chargeable(self):
        settings_eye_examination_chargeable = self.env['ir.config_parameter'].sudo().get_param('eye_examination_chargeable')
        return   settings_eye_examination_chargeable

    eye_examination_chargeable = fields.Boolean(default=default_eye_examination_chargeable,readonly=1)






    prescription_type = fields.Selection([('internal','Internal'),('external','External')],default='internal')
    sph = fields.Selection(
        [('-8.00', '-8.00'), ('-7.75', '-7.75'), ('-7.50', '-7.50'), ('-7.25', '-7.25'), ('-7.00', '-7.00')
            , ('-6.75', '-6.75'), ('-6.50', '-6.50'), ('-6.25', '-6.25'), ('-6.00', '-6.00')
            , ('-5.75', '-5.75'), ('-5.50', '-5.50'), ('-5.25', '-5.25'), ('-5.00', '-5.00')
            , ('-4.75', '-4.75'), ('-4.50', '-4.50'), ('-4.25', '-4.25'), ('-4.00', '-4.00')
            , ('-3.75', '-3.75'), ('-3.50', '-3.50'), ('-3.25', '-3.25'), ('-3.00', '-3.00')
            , ('-2.75', '-2.75'), ('-2.50', '-2.50'), ('-2.25', '-2.25'), ('-2.00', '-2.00')
            , ('-1.75', '-1.75'), ('-1.50', '-1.50'), ('-1.25', '-1.25'), ('-1.00', '-1.00')
            , ('0.75', '-0.75'), ('-0.50', '-0.50'), ('-0.25', '-0.25'), ('-0.00', '-0.00')
            , ('+0.25', '+0.25'), ('+0.50', '+0.50'), ('+0.75', '+0.75'), ('+1.00', '+1.00')
            , ('+1.25', '+1.25'), ('+1.50', '+1.50'), ('+1.75', '+1.75'), ('+2.00', '+2.00')
            , ('+2.25', '+2.25'), ('+2.50', '+2.50'), ('+2.75', '+2.75'), ('+3.00', '+3.00')
            , ('+3.25', '+3.25'), ('+3.50', '+3.50'), ('+3.75', '+3.75'), ('+4.00', '+4.00')
            , ('+4.25', '+4.25'), ('+4.50', '+4.50'), ('+4.75', '+4.75'), ('+5.00', '+5.00')
            , ('+5.25', '+5.25'), ('+5.50', '+5.50'), ('+5.75', '+5.75'), ('+6.00', '+6.00')
            , ('+6.25', '+6.25'), ('+6.50', '+6.50'), ('+6.75', '+6.75'), ('+6.00', '+6.00')

         ], 'Sph')
    cyl = fields.Selection([('-3.50', '-3.50'), ('-3.25', '-3.25'), ('-3.00', '-3.00')
                               , ('-2.75', '-2.75'), ('-2.50', '-2.50'), ('-2.25', '-2.25'), ('-2.00', '-2.00')
                               , ('-1.75', '-1.75'), ('-1.50', '-1.50'), ('-1.25', '-1.25'), ('-1.00', '-1.00')
                               , ('0.75', '-0.75'), ('-0.50', '-0.50'), ('-0.25', '-0.25'), ('-0.00', '-0.00')
                               , ('+0.25', '+0.25'), ('+0.50', '+0.50'), ('+0.25', '+0.25'), ('+1.00', '+1.00')
                               , ('+1.25', '+1.25'), ('+1.50', '+1.50'), ('+1.25', '+1.25'), ('+1.00', '+1.00')
                               , ('+2.25', '+2.25'), ('+2.50', '+2.50'), ('+2.25', '+2.25'), ('+2.00', '+2.00')
                               , ('+3.25', '+3.25'), ('+3.50', '+3.50'), ('+3.75', '+3.75'), ('+4.00', '+4.00')], 'Cyl')
    ax = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
         ('10', '10')
            , ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'),
         ('18', '18'), ('19', '19'), ('20', '20')

            , ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'),
         ('28', '28'), ('29', '29'),
         ('30', '30'), ('31', '31'), ('32', '32')
            ,
         ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'),
         ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'),
         ('49', '49'), ('50', '50'),
         ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'),
         ('59', '59'), ('60', '60'),
         ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'),
         ('69', '60'), ('70', '70'),
         ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'),
         ('79', '79'), ('80', '80'),
         ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'),
         ('89', '89'), ('90', '90'),
         ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'),
         ('99', '99'), ('100', '100'),
         ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'),
         ('108', '108'), ('109', '109'), ('110', '110'), ('111', '111'), ('112', '112'), ('113', '113'), ('114', '114'),
         ('115', '115'), ('116', '116'), ('117', '117'),
         ('118', '118'), ('119', '119'), ('120', '120'), ('121', '121'), ('122', '122'), ('123', '123'), ('124', '124'),
         ('125', '125'), ('126', '126'),
         ('127', '127'), ('128', '128'), ('129', '129'),
         ('130', '130'), ('131', '131'), ('132', '132'),
         ('133', '133'), ('134', '134'), ('135', '135'), ('136', '136'), ('137', '137'), ('138', '138'), ('139', '139'),
         ('140', '140')
            , ('141', '141'), ('142', '142'), ('143', '143'), ('144', '144'), ('145', '145'), ('146', '146'),
         ('147', '147'), ('148', '148'),
         ('149', '149'), ('150', '150'),
         ('151', '151'), ('152', '152'), ('153', '153'), ('154', '154'), ('155', '155'), ('156', '156'), ('157', '157'),
         ('158', '158'),
         ('159', '159'), ('160', '60'),
         ('161', '161'), ('162', '162'), ('163', '163'), ('164', '164'), ('165', '165'), ('1166', '166'),
         ('167', '167'), ('168', '168'),
         ('169', '160'), ('170', '170'),
         ('171', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('175', '175'), ('176', '176'), ('177', '177'),
         ('178', '178'),
         ('179', '79'), ('180', '180')], 'Ax')
    add1 = fields.Selection(
        [('0.00', '0.00'), ('+0.25', '+0.25'), ('+0.50', '+0.50'), ('+0.75', '+0.75'), ('+1.00', '+1.00'),
         ('+1.25', '+1.25'), ('+1.50', '+1.50'),
         ('+1.75', '+1.75'), ('+2.00', '+2.00'), ('+2.25', '+2.25'), ('+2.50', '+2.50'), ('+2.75', '+2.75'),
         ('+3.00', '+3.00'), ('+3.25', '+3.25'), ('+3.50', '+3.50')], 'Add')
    lpd = fields.Float('lpd')
    prism = fields.Boolean('Prism')
    dim = fields.Float('Dim')
    basel = fields.Selection(
        [('Select', 'Select'), ('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
         ], 'basel')
    height = fields.Float('Height')
    sphl = fields.Selection(
        [('-8.00', '-8.00'), ('-7.75', '-7.75'), ('-7.50', '-7.50'), ('-7.25', '-7.25'), ('-7.00', '-7.00')
            , ('-6.75', '-6.75'), ('-6.50', '-6.50'), ('-6.25', '-6.25'), ('-6.00', '-6.00')
            , ('-5.75', '-5.75'), ('-5.50', '-5.50'), ('-5.25', '-5.25'), ('-5.00', '-5.00')
            , ('-4.75', '-4.75'), ('-4.50', '-4.50'), ('-4.25', '-4.25'), ('-4.00', '-4.00')
            , ('-3.75', '-3.75'), ('-3.50', '-3.50'), ('-3.25', '-3.25'), ('-3.00', '-3.00')
            , ('-2.75', '-2.75'), ('-2.50', '-2.50'), ('-2.25', '-2.25'), ('-2.00', '-2.00')
            , ('-1.75', '-1.75'), ('-1.50', '-1.50'), ('-1.25', '-1.25'), ('-1.00', '-1.00')
            , ('0.75', '-0.75'), ('-0.50', '-0.50'), ('-0.25', '-0.25'), ('-0.00', '-0.00')
            , ('+0.25', '+0.25'), ('+0.50', '+0.50'), ('+0.75', '+0.75'), ('+1.00', '+1.00')
            , ('+1.25', '+1.25'), ('+1.50', '+1.50'), ('+1.75', '+1.75'), ('+2.00', '+2.00')
            , ('+2.25', '+2.25'), ('+2.50', '+2.50'), ('+2.75', '+2.75'), ('+3.00', '+3.00')
            , ('+3.25', '+3.25'), ('+3.50', '+3.50'), ('+3.75', '+3.75'), ('+4.00', '+4.00')
            , ('+4.25', '+4.25'), ('+4.50', '+4.50'), ('+4.75', '+4.75'), ('+5.00', '+5.00')
            , ('+5.25', '+5.25'), ('+5.50', '+5.50'), ('+5.75', '+5.75'), ('+6.00', '+6.00')
            , ('+6.25', '+6.25'), ('+6.50', '+6.50'), ('+6.75', '+6.75'), ('+6.00', '+6.00')

         ], 'Sphl')
    cyll = fields.Selection([('-3.50', '-3.50'), ('-3.25', '-3.25'), ('-3.00', '-3.00')
                                , ('-2.75', '-2.75'), ('-2.50', '-2.50'), ('-2.25', '-2.25'), ('-2.00', '-2.00')
                                , ('-1.75', '-1.75'), ('-1.50', '-1.50'), ('-1.25', '-1.25'), ('-1.00', '-1.00')
                                , ('0.75', '-0.75'), ('-0.50', '-0.50'), ('-0.25', '-0.25'), ('-0.00', '-0.00')
                                , ('+0.25', '+0.25'), ('+0.50', '+0.50'), ('+0.25', '+0.25'), ('+1.00', '+1.00')
                                , ('+1.25', '+1.25'), ('+1.50', '+1.50'), ('+1.25', '+1.25'), ('+1.00', '+1.00')
                                , ('+1.25', '+1.25'), ('+1.50', '+1.50'), ('+1.25', '+1.25'), ('+1.00', '+1.00')
                                , ('+2.25', '+2.25'), ('+2.50', '+2.50'), ('+2.25', '+2.25'), ('+2.00', '+2.00')
                                , ('+3.25', '+3.25'), ('+3.50', '+3.50'), ('+3.75', '+3.75'), ('+4.00', '+4.00'
                                                                                               )], 'Cyll')
    axl = fields.Selection([
        ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
        ('10', '10')
        , ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'),
        ('18', '18'), ('19', '19'), ('20', '20')

        , ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'),
        ('28', '28'), ('29', '29'),
        ('30', '30'), ('31', '31'), ('32', '32')
        ,
        ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'),
        ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('47', '47'), ('48', '48'),
        ('49', '49'), ('50', '50'),
        ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'), ('58', '58'),
        ('59', '59'), ('60', '60'),
        ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'), ('68', '68'),
        ('69', '60'), ('70', '70'),
        ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'), ('78', '78'),
        ('79', '79'), ('80', '80'),
        ('81', '81'), ('82', '82'), ('83', '83'), ('84', '84'), ('85', '85'), ('86', '86'), ('87', '87'), ('88', '88'),
        ('89', '89'), ('90', '90'),
        ('91', '91'), ('92', '92'), ('93', '93'), ('94', '94'), ('95', '95'), ('96', '96'), ('97', '97'), ('98', '98'),
        ('99', '99'), ('100', '100'),
        ('101', '101'), ('102', '102'), ('103', '103'), ('104', '104'), ('105', '105'), ('106', '106'), ('107', '107'),
        ('108', '108'), ('109', '109'), ('110', '110'), ('111', '111'), ('112', '112'), ('113', '113'), ('114', '114'),
        ('115', '115'), ('116', '116'), ('117', '117'),
        ('118', '118'), ('119', '119'), ('120', '120'), ('121', '121'), ('122', '122'), ('123', '123'), ('124', '124'),
        ('125', '125'), ('126', '126'),
        ('127', '127'), ('128', '128'), ('129', '129'),
        ('130', '130'), ('131', '131'), ('132', '132'),
        ('133', '133'), ('134', '134'), ('135', '135'), ('136', '136'), ('137', '137'), ('138', '138'), ('139', '139'),
        ('140', '140')
        , ('141', '141'), ('142', '142'), ('143', '143'), ('144', '144'), ('145', '145'), ('146', '146'),
        ('147', '147'), ('148', '148'),
        ('149', '149'), ('150', '150'),
        ('151', '151'), ('152', '152'), ('153', '153'), ('154', '154'), ('155', '155'), ('156', '156'), ('157', '157'),
        ('158', '158'),
        ('159', '159'), ('160', '60'),
        ('161', '161'), ('162', '162'), ('163', '163'), ('164', '164'), ('165', '165'), ('1166', '166'), ('167', '167'),
        ('168', '168'),
        ('169', '160'), ('170', '170'),
        ('171', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('175', '175'), ('176', '176'), ('177', '177'),
        ('178', '178'),
        ('179', '79'), ('180', '180')], 'Axl')
    add1l = fields.Selection(
        [('0.00', '0.00'), ('+0.25', '+0.25'), ('+0.50', '+0.50'), ('+0.75', '+0.75'), ('+1.00', '+1.00'),
         ('+1.25', '+1.25'), ('+1.50', '+1.50'),
         ('+1.75', '+1.75'), ('+2.00', '+2.00'), ('+2.25', '+2.25'), ('+2.50', '+2.50'), ('+2.75', '+2.75'),
         ('+3.00', '+3.00'), ('+3.25', '+3.25'), ('+3.50', '+3.50')], 'Addl')

    lpdl = fields.Float('lpd')
    prisml = fields.Float('Prism')
    diml = fields.Float('Dim')
    baser = fields.Selection(
        [('Select', 'Select'), ('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
         ], 'baser')
    heightl = fields.Float('Height')
    prism_vall = fields.Selection(
        [('0.25', '0.25'), ('0.50', '0.50'), ('0.75', '0.75'), ('1.00', '1.00'),
         ('1.25', '1.25'), ('1.50', '1.50'),
         ('1.75', '1.75'), ('2.00', '2.00'), ('2.25', '2.25'), ('2.50', '2.50'), ('2.75', '2.75'),
         ('3.00', '3.00'), ('3.25', '3.25'), ('3.50', '3.50'), ('3.75', '3.75'), ('4.00', '4.00'), ('4.25', '4.25'),
         ('4.50', '4.50'), ('4.75', '4.75'),
         ('5.00', '5.00')], 'PrismL')

    prism_valr = fields.Selection(
        [('0.25', '0.25'), ('0.50', '0.50'), ('0.75', '0.75'), ('1.00', '1.00'),
         ('1.25', '1.25'), ('1.50', '1.50'),
         ('1.75', '1.75'), ('2.00', '2.00'), ('2.25', '2.25'), ('2.50', '2.50'), ('2.75', '2.75'),
         ('3.00', '3.00'), ('3.25', '3.25'), ('3.50', '3.50'), ('3.75', '3.75'), ('4.00', '4.00'), ('4.25', '4.25'),
         ('4.50', '4.50'), ('4.75', '4.75'),
         ('5.00', '5.00')], 'PrismR')

    dual_pd = fields.Boolean('I have Dual PD')
    pd = fields.Selection(
        [('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'),
         ('60', '60'), ('70', '70')
            , ('79', '79')], 'PD')
    pdl = fields.Selection(
        [('31.5', '31.5'), ('31', '31'), ('30.5', '30.5'), ('30', '30'),
         ('29.5', '29.5'), ('29', '29')
            , ('28.5', '28.5'), ('28', '28')], 'PDL')
    pdr = fields.Selection(
        [('31.5', '31.5'), ('31', '31'), ('30.5', '30.5'), ('30', '30'),
         ('29.5', '29.5'), ('29', '29')
            , ('28.5', '28.5'), ('28', '28')], 'PDR')

    dr_notes = fields.Text('Notes')
    name = fields.Char(required=True, copy=False, readonly=True,index=True, default=lambda self: _('New'))
    family_eye_history = fields.Text()
    ocular_history = fields.Text()
    consultation = fields.Text()

    def open_customer(self):
        sale_order=self.env['sale.order'].search([('prescription_id','=',self.id)],limit=1)
        print('fire',sale_order)
        if sale_order:
            return {
                'name':_('Doctor Prescription'),
                'view_type': 'form',
                'res_id':sale_order.id,
                'res_model': 'sale.order',
                'view_id': False,
                'view_mode':'form',
                # 'context':{'default_dr':self.id},
                'type': 'ir.actions.act_window',
            }



        else:
            return {
                'name':_('Doctor Prescription'),
                'view_type': 'form',
                'res_model': 'sale.order',
                'view_id': False,
                'view_mode':'form',
                'context':{'default_prescription_id':self.id,'default_partner_id':self.customer.id},
                'type': 'ir.actions.act_window',
            }




    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('optical.prescription.sequence')
        result = super(DrPrescription,self).create(vals)
        return result


    def print_prescription_report(self):
            return {
                'type': 'ir.actions.report',
                'report_name': "optical_erp.doctor_prescription_template",
                'report_file': "optical_erp.doctor_prescription_template",
                'report_type': 'qweb-pdf',
            }







