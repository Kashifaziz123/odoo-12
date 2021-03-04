from odoo import api, fields, models, _
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
    diagnosis_client = fields.Text()
    notes_laboratory = fields.Text()
    optometrist_observation = fields.Text()
    state = fields.Selection([('Draft','Draft'),('Confirm','Confirm')],default='Draft')

    def confirm_request(self):
        for rec in self:
            rec.state = 'Confirm'


    def default_eye_examination_chargeable(self):
        settings_eye_examination_chargeable = self.env['ir.config_parameter'].sudo().get_param('eye_examination_chargeable')
        return   settings_eye_examination_chargeable

    eye_examination_chargeable = fields.Boolean(default=default_eye_examination_chargeable,readonly=1)

    prescription_type = fields.Selection([('Internal','Internal'),('External','External')],default='internal')
    # OD
    od_sph_distance = fields.Selection(
        [('0','0'),('-16', '-16'),('-15.75','-15.75'),('-15.5','-15.5'),('-15.25','-15.25'),('-15','-15'),
         ('-14.75','-14.75'), ('-14.5','-14.5'), ('-14.25','-14.25'), ('-14','-14'),
         ('-13.75','-13.75'), ('-13.5','-13.5'),('-13.25','-13.25'), ('-13','-13'),
         ('-12.75','-12.75'), ('-12.5','-12.5'),('-12.25','-12.25'), ('-12','-12'),
         ('-11.75','-11.75'), ('-11.5','-11.5'), ('-11.25','-11.25'), ('-11','-11'),
         ('-10.75','-10.75'), ('-10.5','-10.5'), ('-10.25','-10.25'), ('-10','-10'),
         ('-9.75','-9.75'), ('-9.5','-9.5'), ('-9.25','-9.25'), ('-9','-9'),
         ('-8.75','-8.75'), ('-8.5','-8.5'), ('-8.25','-8.25'), ('-8','-8'),
         ('-7.75','-7.75'), ('-7.5','-7.5'), ('-7.25','-7.25'), ('-7','-7'),
         ('-6.75','-6.75'), ('-6.5','-6.5'), ('-6.25','-6.25'), ('-6','-6'),
         ('-5.75','-5.75'), ('-5.5','-5.5'), ('-5.25','-5.25'), ('-5','-5'),
         ('-4.75','-4.75'), ('-4.5','-4.5'), ('-4.25','-4.25'), ('-4','-4'),
         ('-3.75','-3.75'), ('-3.5','-3.5'), ('-3.25','-3.25'), ('-3','-3'),
         ('-2.75','-2.75'), ('-2.5','-2.5'), ('-2.25','-2.25'), ('-2','-2'),
         ('-1.75','-1.75'), ('-1.5','-1.5'), ('-1.25','-1.25'), ('-1','-1'),
         ('-0.75','-0.75'), ('-0.5','-0.5'), ('-0.25','-0.25'), ('-0','-0'),
         ('+0','+0'),('+0.25','+0.25'),('+0.5','+0.5'),('+0.75','+0.75'),
         ('+1', '+1'), ('+1.25','+1.25'), ('+1.5','+1.5'), ('+1.75','+1.75'),
         ('+2','+2'), ('+2.25','+2.25'), ('+2.5','+2.5'), ('+2.75','+2.75'),
         ('+3','+3'), ('+3.25','+3.25'), ('+3.5','+3.5'), ('+3.75','+3.75'),
         ('+4','+4'), ('+4.25','+4.25'), ('+4.5','+4.5'), ('+4.75','+4.75'),
         ('+5','+5'), ('+5.25','+5.25'), ('+5.5','+5.5'), ('+5.75','+5.75'),
         ('+6','+6'), ('+6.25','+6.25'), ('+6.5','+6.5'), ('+6.75','+6.75'),
         ('+7','+7'), ('+7.25','+7.25'), ('+7.5','+7.5'), ('+7.75','+7.75'),
         ('+8','+8'), ('+8.25','+8.25'), ('+8.5','+8.5'), ('+8.75','+8.75'),
         ('+9','+9'), ('+9.25','+9.25'), ('+9.5','+9.5'), ('+9.75','+9.75'),
         ('+10','+10'), ('+10.25','+10.25'), ('+10.5','+10.5'), ('+10.75','+10.75'),
         ('+11','+11'), ('+11.25','+11.25'), ('+11.5','+11.5'), ('+11.75','+11.75'),
         ('+12','+12')
         ],default='0')
    od_sph_near = fields.Selection(
        [('0', '0'), ('-16', '-16'), ('-15.75', '-15.75'), ('-15.5', '-15.5'), ('-15.25', '-15.25'),
         ('-15', '-15'),
         ('-14.75', '-14.75'), ('-14.5', '-14.5'), ('-14.25', '-14.25'), ('-14', '-14'),
         ('-13.75', '-13.75'), ('-13.5', '-13.5'), ('-13.25', '-13.25'), ('-13', '-13'),
         ('-12.75', '-12.75'), ('-12.5', '-12.5'), ('-12.25', '-12.25'), ('-12', '-12'),
         ('-11.75', '-11.75'), ('-11.5', '-11.5'), ('-11.25', '-11.25'), ('-11', '-11'),
         ('-10.75', '-10.75'), ('-10.5', '-10.5'), ('-10.25', '-10.25'), ('-10', '-10'),
         ('-9.75', '-9.75'), ('-9.5', '-9.5'), ('-9.25', '-9.25'), ('-9', '-9'),
         ('-8.75', '-8.75'), ('-8.5', '-8.5'), ('-8.25', '-8.25'), ('-8', '-8'),
         ('-7.75', '-7.75'), ('-7.5', '-7.5'), ('-7.25', '-7.25'), ('-7', '-7'),
         ('-6.75', '-6.75'), ('-6.5', '-6.5'), ('-6.25', '-6.25'), ('-6', '-6'),
         ('-5.75', '-5.75'), ('-5.5', '-5.5'), ('-5.25', '-5.25'), ('-5', '-5'),
         ('-4.75', '-4.75'), ('-4.5', '-4.5'), ('-4.25', '-4.25'), ('-4', '-4'),
         ('-3.75', '-3.75'), ('-3.5', '-3.5'), ('-3.25', '-3.25'), ('-3', '-3'),
         ('-2.75', '-2.75'), ('-2.5', '-2.5'), ('-2.25', '-2.25'), ('-2', '-2'),
         ('-1.75', '-1.75'), ('-1.5', '-1.5'), ('-1.25', '-1.25'), ('-1', '-1'),
         ('-0.75', '-0.75'), ('-0.5', '-0.5'), ('-0.25', '-0.25'), ('-0', '-0'),
         ('+0', '+0'), ('+0.25', '+0.25'), ('+0.5', '+0.5'), ('+0.75', '+0.75'),
         ('+1', '+1'), ('+1.25', '+1.25'), ('+1.5', '+1.5'), ('+1.75', '+1.75'),
         ('+2', '+2'), ('+2.25', '+2.25'), ('+2.5', '+2.5'), ('+2.75', '+2.75'),
         ('+3', '+3'), ('+3.25', '+3.25'), ('+3.5', '+3.5'), ('+3.75', '+3.75'),
         ('+4', '+4'), ('+4.25', '+4.25'), ('+4.5', '+4.5'), ('+4.75', '+4.75'),
         ('+5', '+5'), ('+5.25', '+5.25'), ('+5.5', '+5.5'), ('+5.75', '+5.75'),
         ('+6', '+6'), ('+6.25', '+6.25'), ('+6.5', '+6.5'), ('+6.75', '+6.75'),
         ('+7', '+7'), ('+7.25', '+7.25'), ('+7.5', '+7.5'), ('+7.75', '+7.75'),
         ('+8', '+8'), ('+8.25', '+8.25'), ('+8.5', '+8.5'), ('+8.75', '+8.75'),
         ('+9', '+9'), ('+9.25', '+9.25'), ('+9.5', '+9.5'), ('+9.75', '+9.75'),
         ('+10', '+10'), ('+10.25', '+10.25'), ('+10.5', '+10.5'), ('+10.75', '+10.75'),
         ('+11', '+11'), ('+11.25', '+11.25'), ('+11.5', '+11.5'), ('+11.75', '+11.75'),
         ('+12', '+12')
         ], default='0')
    od_cyl_distance = fields.Selection(
        [('0','0'),('-6', '-6'),
         ('-5.75', '-5.75'), ('-5.5', '-5.5'), ('-5.25', '-5.25'), ('-5', '-5'),
         ('-4.75', '-4.75'), ('-4.5', '-4.5'), ('-4.25', '-4.25'), ('-4', '-4'),
         ('-3.75', '-3.75'), ('-3.5', '-3.5'), ('-3.25', '-3.25'), ('-3', '-3'),
         ('-2.75', '-2.75'), ('-2.5', '-2.5'), ('-2.25', '-2.25'), ('-2', '-2'),
         ('-1.75', '-1.75'), ('-1.5', '-1.5'), ('-1.25', '-1.25'), ('-1', '-1'),
         ('-0.75', '-0.75'), ('-0.5', '-0.5'), ('-0.25', '-0.25'), ('-0', '-0'),
         ('+0', '+0'), ('+0.25', '+0.25'), ('+0.5', '+0.5'), ('+0.75', '+0.75'),
         ('+1', '+1'), ('+1.25', '+1.25'), ('+1.5', '+1.5'), ('+1.75', '+1.75'),
         ('+2', '+2'), ('+2.25', '+2.25'), ('+2.5', '+2.5'), ('+2.75', '+2.75'),
         ('+3', '+3'), ('+3.25', '+3.25'), ('+3.5', '+3.5'), ('+3.75', '+3.75'),
         ('+4', '+4'), ('+4.25', '+4.25'), ('+4.5', '+4.5'), ('+4.75', '+4.75'),
         ('+5', '+5'), ('+5.25', '+5.25'), ('+5.5', '+5.5'), ('+5.75', '+5.75'),
         ('+6', '+6')
         ],default='0')
    od_cyl_near = fields.Selection(
        [('0','0'),('-6', '-6'),
         ('-5.75', '-5.75'), ('-5.5', '-5.5'), ('-5.25', '-5.25'), ('-5', '-5'),
         ('-4.75', '-4.75'), ('-4.5', '-4.5'), ('-4.25', '-4.25'), ('-4', '-4'),
         ('-3.75', '-3.75'), ('-3.5', '-3.5'), ('-3.25', '-3.25'), ('-3', '-3'),
         ('-2.75', '-2.75'), ('-2.5', '-2.5'), ('-2.25', '-2.25'), ('-2', '-2'),
         ('-1.75', '-1.75'), ('-1.5', '-1.5'), ('-1.25', '-1.25'), ('-1', '-1'),
         ('-0.75', '-0.75'), ('-0.5', '-0.5'), ('-0.25', '-0.25'), ('-0', '-0'),
         ('+0', '+0'), ('+0.25', '+0.25'), ('+0.5', '+0.5'), ('+0.75', '+0.75'),
         ('+1', '+1'), ('+1.25', '+1.25'), ('+1.5', '+1.5'), ('+1.75', '+1.75'),
         ('+2', '+2'), ('+2.25', '+2.25'), ('+2.5', '+2.5'), ('+2.75', '+2.75'),
         ('+3', '+3'), ('+3.25', '+3.25'), ('+3.5', '+3.5'), ('+3.75', '+3.75'),
         ('+4', '+4'), ('+4.25', '+4.25'), ('+4.5', '+4.5'), ('+4.75', '+4.75'),
         ('+5', '+5'), ('+5.25', '+5.25'), ('+5.5', '+5.5'), ('+5.75', '+5.75'),
         ('+6', '+6')
         ],default='0')
    od_ax_distance = fields.Selection(
        [('0', '0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
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
            , ('141', '141'), ('142', '142'), ('143', '143'), ('144','144'), ('145', '145'), ('146', '146'),
         ('147', '147'), ('148', '148'),
         ('149', '149'), ('150', '150'),
         ('151', '151'), ('152', '152'), ('153', '153'), ('154', '154'), ('155', '155'), ('156', '156'), ('157', '157'),
         ('158', '158'),
         ('159', '159'), ('160', '160'),
         ('161', '161'), ('162', '162'), ('163', '163'), ('164', '164'), ('165', '165'), ('166', '166'),
         ('167', '167'), ('168', '168'),
         ('169', '169'), ('170', '170'),
         ('171', '171'), ('172', '172'), ('173', '173'), ('174', '174'), ('175', '175'), ('176', '176'), ('177', '177'),
         ('178', '178'),
         ('179', '179'), ('180', '180')],default='0')
    od_ax_near = fields.Selection(
        [('0', '0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
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
            , ('141', '141'), ('142', '142'), ('143', '143'), ('144','144'), ('145', '145'), ('146', '146'),
         ('147', '147'), ('148', '148'),
         ('149', '149'), ('150', '150'),
         ('151', '151'), ('152', '152'), ('153', '153'), ('154', '154'), ('155', '155'), ('156', '156'), ('157', '157'),
         ('158', '158'),
         ('159', '159'), ('160', '160'),
         ('161', '161'), ('162', '162'), ('163', '163'), ('164', '164'), ('165', '165'), ('166', '166'),
         ('167', '167'), ('168', '168'),
         ('169', '169'), ('170', '170'),
         ('171', '171'), ('172', '172'), ('173', '173'), ('174', '174'), ('175', '175'), ('176', '176'), ('177', '177'),
         ('178', '178'),
         ('179', '179'), ('180', '180')],default='0')
    od_add_distance = fields.Selection(
        [('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'),
         ('4', '4'), ('4.25', '4.25'), ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5'), ('5.25', '5.25'), ('5.5', '5.5'), ('5.75', '5.75'),
         ('6', '6')
         ],default='0')
    od_add_near = fields.Selection(
        [('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'),
         ('4', '4'), ('4.25', '4.25'), ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5'), ('5.25', '5.25'), ('5.5', '5.5'), ('5.75', '5.75'),
         ('6', '6')
         ],default='0')
    od_prism_distance = fields.Selection(
        [('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'), ('3.75', '3.75'), ('4', '4'), ('4.25', '4.25'),
         ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5')], 'PrismR')
    od_prism_near = fields.Selection(
        [('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'), ('3.75', '3.75'), ('4', '4'), ('4.25', '4.25'),
         ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5')], 'PrismR')
    od_base_distance = fields.Selection(
        [('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
         ], 'baser')
    od_base_near = fields.Selection(
        [ ('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
         ], 'baser')
    # OS
    os_sph_distance = fields.Selection(
        [('0','0'),('-16', '-16'),('-15.75','-15.75'),('-15.5','-15.5'),('-15.25','-15.25'),('-15','-15'),
         ('-14.75','-14.75'), ('-14.5','-14.5'), ('-14.25','-14.25'), ('-14','-14'),
         ('-13.75','-13.75'), ('-13.5','-13.5'),('-13.25','-13.25'), ('-13','-13'),
         ('-12.75','-12.75'), ('-12.5','-12.5'),('-12.25','-12.25'), ('-12','-12'),
         ('-11.75','-11.75'), ('-11.5','-11.5'), ('-11.25','-11.25'), ('-11','-11'),
         ('-10.75','-10.75'), ('-10.5','-10.5'), ('-10.25','-10.25'), ('-10','-10'),
         ('-9.75','-9.75'), ('-9.5','-9.5'), ('-9.25','-9.25'), ('-9','-9'),
         ('-8.75','-8.75'), ('-8.5','-8.5'), ('-8.25','-8.25'), ('-8','-8'),
         ('-7.75','-7.75'), ('-7.5','-7.5'), ('-7.25','-7.25'), ('-7','-7'),
         ('-6.75','-6.75'), ('-6.5','-6.5'), ('-6.25','-6.25'), ('-6','-6'),
         ('-5.75','-5.75'), ('-5.5','-5.5'), ('-5.25','-5.25'), ('-5','-5'),
         ('-4.75','-4.75'), ('-4.5','-4.5'), ('-4.25','-4.25'), ('-4','-4'),
         ('-3.75','-3.75'), ('-3.5','-3.5'), ('-3.25','-3.25'), ('-3','-3'),
         ('-2.75','-2.75'), ('-2.5','-2.5'), ('-2.25','-2.25'), ('-2','-2'),
         ('-1.75','-1.75'), ('-1.5','-1.5'), ('-1.25','-1.25'), ('-1','-1'),
         ('-0.75','-0.75'), ('-0.5','-0.5'), ('-0.25','-0.25'), ('-0','-0'),
         ('+0','+0'),('+0.25','+0.25'),('+0.5','+0.5'),('+0.75','+0.75'),
         ('+1', '+1'), ('+1.25','+1.25'), ('+1.5','+1.5'), ('+1.75','+1.75'),
         ('+2','+2'), ('+2.25','+2.25'), ('+2.5','+2.5'), ('+2.75','+2.75'),
         ('+3','+3'), ('+3.25','+3.25'), ('+3.5','+3.5'), ('+3.75','+3.75'),
         ('+4','+4'), ('+4.25','+4.25'), ('+4.5','+4.5'), ('+4.75','+4.75'),
         ('+5','+5'), ('+5.25','+5.25'), ('+5.5','+5.5'), ('+5.75','+5.75'),
         ('+6','+6'), ('+6.25','+6.25'), ('+6.5','+6.5'), ('+6.75','+6.75'),
         ('+7','+7'), ('+7.25','+7.25'), ('+7.5','+7.5'), ('+7.75','+7.75'),
         ('+8','+8'), ('+8.25','+8.25'), ('+8.5','+8.5'), ('+8.75','+8.75'),
         ('+9','+9'), ('+9.25','+9.25'), ('+9.5','+9.5'), ('+9.75','+9.75'),
         ('+10','+10'), ('+10.25','+10.25'), ('+10.5','+10.5'), ('+10.75','+10.75'),
         ('+11','+11'), ('+11.25','+11.25'), ('+11.5','+11.5'), ('+11.75','+11.75'),
         ('+12','+12')
         ],default='0')
    os_sph_near = fields.Selection(
        [('0','0'),('-16', '-16'),('-15.75','-15.75'),('-15.5','-15.5'),('-15.25','-15.25'),('-15','-15'),
         ('-14.75','-14.75'), ('-14.5','-14.5'), ('-14.25','-14.25'), ('-14','-14'),
         ('-13.75','-13.75'), ('-13.5','-13.5'),('-13.25','-13.25'), ('-13','-13'),
         ('-12.75','-12.75'), ('-12.5','-12.5'),('-12.25','-12.25'), ('-12','-12'),
         ('-11.75','-11.75'), ('-11.5','-11.5'), ('-11.25','-11.25'), ('-11','-11'),
         ('-10.75','-10.75'), ('-10.5','-10.5'), ('-10.25','-10.25'), ('-10','-10'),
         ('-9.75','-9.75'), ('-9.5','-9.5'), ('-9.25','-9.25'), ('-9','-9'),
         ('-8.75','-8.75'), ('-8.5','-8.5'), ('-8.25','-8.25'), ('-8','-8'),
         ('-7.75','-7.75'), ('-7.5','-7.5'), ('-7.25','-7.25'), ('-7','-7'),
         ('-6.75','-6.75'), ('-6.5','-6.5'), ('-6.25','-6.25'), ('-6','-6'),
         ('-5.75','-5.75'), ('-5.5','-5.5'), ('-5.25','-5.25'), ('-5','-5'),
         ('-4.75','-4.75'), ('-4.5','-4.5'), ('-4.25','-4.25'), ('-4','-4'),
         ('-3.75','-3.75'), ('-3.5','-3.5'), ('-3.25','-3.25'), ('-3','-3'),
         ('-2.75','-2.75'), ('-2.5','-2.5'), ('-2.25','-2.25'), ('-2','-2'),
         ('-1.75','-1.75'), ('-1.5','-1.5'), ('-1.25','-1.25'), ('-1','-1'),
         ('-0.75','-0.75'), ('-0.5','-0.5'), ('-0.25','-0.25'), ('-0','-0'),
         ('+0','+0'),('+0.25','+0.25'),('+0.5','+0.5'),('+0.75','+0.75'),
         ('+1', '+1'), ('+1.25','+1.25'), ('+1.5','+1.5'), ('+1.75','+1.75'),
         ('+2','+2'), ('+2.25','+2.25'), ('+2.5','+2.5'), ('+2.75','+2.75'),
         ('+3','+3'), ('+3.25','+3.25'), ('+3.5','+3.5'), ('+3.75','+3.75'),
         ('+4','+4'), ('+4.25','+4.25'), ('+4.5','+4.5'), ('+4.75','+4.75'),
         ('+5','+5'), ('+5.25','+5.25'), ('+5.5','+5.5'), ('+5.75','+5.75'),
         ('+6','+6'), ('+6.25','+6.25'), ('+6.5','+6.5'), ('+6.75','+6.75'),
         ('+7','+7'), ('+7.25','+7.25'), ('+7.5','+7.5'), ('+7.75','+7.75'),
         ('+8','+8'), ('+8.25','+8.25'), ('+8.5','+8.5'), ('+8.75','+8.75'),
         ('+9','+9'), ('+9.25','+9.25'), ('+9.5','+9.5'), ('+9.75','+9.75'),
         ('+10','+10'), ('+10.25','+10.25'), ('+10.5','+10.5'), ('+10.75','+10.75'),
         ('+11','+11'), ('+11.25','+11.25'), ('+11.5','+11.5'), ('+11.75','+11.75'),
         ('+12','+12')
         ],default='0')
    os_cyl_distance = fields.Selection(
        [('0','0'),('-6', '-6'),
         ('-5.75', '-5.75'), ('-5.5', '-5.5'), ('-5.25', '-5.25'), ('-5', '-5'),
         ('-4.75', '-4.75'), ('-4.5', '-4.5'), ('-4.25', '-4.25'), ('-4', '-4'),
         ('-3.75', '-3.75'), ('-3.5', '-3.5'), ('-3.25', '-3.25'), ('-3', '-3'),
         ('-2.75', '-2.75'), ('-2.5', '-2.5'), ('-2.25', '-2.25'), ('-2', '-2'),
         ('-1.75', '-1.75'), ('-1.5', '-1.5'), ('-1.25', '-1.25'), ('-1', '-1'),
         ('-0.75', '-0.75'), ('-0.5', '-0.5'), ('-0.25', '-0.25'), ('-0', '-0'),
         ('+0', '+0'), ('+0.25', '+0.25'), ('+0.5', '+0.5'), ('+0.75', '+0.75'),
         ('+1', '+1'), ('+1.25', '+1.25'), ('+1.5', '+1.5'), ('+1.75', '+1.75'),
         ('+2', '+2'), ('+2.25', '+2.25'), ('+2.5', '+2.5'), ('+2.75', '+2.75'),
         ('+3', '+3'), ('+3.25', '+3.25'), ('+3.5', '+3.5'), ('+3.75', '+3.75'),
         ('+4', '+4'), ('+4.25', '+4.25'), ('+4.5', '+4.5'), ('+4.75', '+4.75'),
         ('+5', '+5'), ('+5.25', '+5.25'), ('+5.5', '+5.5'), ('+5.75', '+5.75'),
         ('+6', '+6')

         ],default='0')
    os_cyl_near = fields.Selection(
        [('0','0'),('-6', '-6'),
         ('-5.75', '-5.75'), ('-5.5', '-5.5'), ('-5.25', '-5.25'), ('-5', '-5'),
         ('-4.75', '-4.75'), ('-4.5', '-4.5'), ('-4.25', '-4.25'), ('-4', '-4'),
         ('-3.75', '-3.75'), ('-3.5', '-3.5'), ('-3.25', '-3.25'), ('-3', '-3'),
         ('-2.75', '-2.75'), ('-2.5', '-2.5'), ('-2.25', '-2.25'), ('-2', '-2'),
         ('-1.75', '-1.75'), ('-1.5', '-1.5'), ('-1.25', '-1.25'), ('-1', '-1'),
         ('-0.75', '-0.75'), ('-0.5', '-0.5'), ('-0.25', '-0.25'), ('-0', '-0'),
         ('+0', '+0'), ('+0.25', '+0.25'), ('+0.5', '+0.5'), ('+0.75', '+0.75'),
         ('+1', '+1'), ('+1.25', '+1.25'), ('+1.5', '+1.5'), ('+1.75', '+1.75'),
         ('+2', '+2'), ('+2.25', '+2.25'), ('+2.5', '+2.5'), ('+2.75', '+2.75'),
         ('+3', '+3'), ('+3.25', '+3.25'), ('+3.5', '+3.5'), ('+3.75', '+3.75'),
         ('+4', '+4'), ('+4.25', '+4.25'), ('+4.5', '+4.5'), ('+4.75', '+4.75'),
         ('+5', '+5'), ('+5.25', '+5.25'), ('+5.5', '+5.5'), ('+5.75', '+5.75'),
         ('+6', '+6')

         ],default='0')
    os_ax_distance = fields.Selection(
        [('0', '0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
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
            , ('141', '141'), ('142', '142'), ('143', '143'), ('144','144'), ('145', '145'), ('146', '146'),
         ('147', '147'), ('148', '148'),
         ('149', '149'), ('150', '150'),
         ('151', '151'), ('152', '152'), ('153', '153'), ('154', '154'), ('155', '155'), ('156', '156'), ('157', '157'),
         ('158', '158'),
         ('159', '159'), ('160', '160'),
         ('161', '161'), ('162', '162'), ('163', '163'), ('164', '164'), ('165', '165'), ('166', '166'),
         ('167', '167'), ('168', '168'),
         ('169', '169'), ('170', '170'),
         ('171', '171'), ('172', '172'), ('173', '173'), ('174', '174'), ('175', '175'), ('176', '176'), ('177', '177'),
         ('178', '178'),
         ('179', '179'), ('180', '180')],default='0')
    os_ax_near = fields.Selection(
        [('0', '0'),('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'),
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
            , ('141', '141'), ('142', '142'), ('143', '143'), ('144','144'), ('145', '145'), ('146', '146'),
         ('147', '147'), ('148', '148'),
         ('149', '149'), ('150', '150'),
         ('151', '151'), ('152', '152'), ('153', '153'), ('154', '154'), ('155', '155'), ('156', '156'), ('157', '157'),
         ('158', '158'),
         ('159', '159'), ('160', '160'),
         ('161', '161'), ('162', '162'), ('163', '163'), ('164', '164'), ('165', '165'), ('166', '166'),
         ('167', '167'), ('168', '168'),
         ('169', '169'), ('170', '170'),
         ('171', '171'), ('172', '172'), ('173', '173'), ('174', '174'), ('175', '175'), ('176', '176'), ('177', '177'),
         ('178', '178'),
         ('179', '179'), ('180', '180')],default='0')
    os_add_distance = fields.Selection(
        [('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'),
         ('4', '4'), ('4.25', '4.25'), ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5'), ('5.25', '5.25'), ('5.5', '5.5'), ('5.75', '5.75'),
         ('6', '6')
         ],default='0')
    os_add_near = fields.Selection(
        [('0', '0'), ('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'),
         ('4', '4'), ('4.25', '4.25'), ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5'), ('5.25', '5.25'), ('5.5', '5.5'), ('5.75', '5.75'),
         ('6', '6')
         ],default='0')
    os_prism_distance = fields.Selection(
        [('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'), ('3.75', '3.75'), ('4', '4'), ('4.25', '4.25'),
         ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5')], 'PrismR')
    os_prism_near = fields.Selection(
        [('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
         ('1.25', '1.25'), ('1.5', '1.5'),
         ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
         ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'), ('3.75', '3.75'), ('4', '4'), ('4.25', '4.25'),
         ('4.5', '4.5'), ('4.75', '4.75'),
         ('5', '5')], 'PrismR')
    os_base_distance = fields.Selection(
        [('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
         ], 'baser')
    os_base_near = fields.Selection(
        [('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
         ], 'baser')
    # Extras
    dual_pd = fields.Boolean('I have Dual PD')
    pd = fields.Selection(
        [
            ('50', '50'),
            ('51', '51'), ('52', '52'), ('53', '53'), ('54', '54'), ('55', '55'), ('56', '56'), ('57', '57'),
            ('58', '58'),
            ('59', '59'),
            ('60', '60'),
            ('61', '61'), ('62', '62'), ('63', '63'), ('64', '64'), ('65', '65'), ('66', '66'), ('67', '67'),
            ('68', '68'),
            ('69', '69'), ('70', '70'),
            ('71', '71'), ('72', '72'), ('73', '73'), ('74', '74'), ('75', '75'), ('76', '76'), ('77', '77'),
            ('78', '78'),
            ('79', '79'), ('80', '80')
        ],default='60')
    pdl = fields.Selection(
        [('40', '40'), ('39.5', '39.5'), ('39', '39'), ('38.5', '38.5'), ('38', '38'), ('37.5', '37.5'), ('37', '37'), ('36.5', '36.5'), ('36', '36'), ('35.5', '35.5'),
        ('35', '35'), ('34.5', '34.5'), ('34', '34'), ('33.5', '33.5'), ('33', '33'), ('32.5', '32.5'), ('32', '32'), ('31.5', '31.5'), ('31', '31'), ('30.5', '30.5'),
        ('20', '20'), ('29.5', '29.5'), ('29', '29'), ('28.5', '28.5'), ('28', '28'), ('27.5', '27.5'), ('27', '27'), ('26.5', '26.5'), ('26', '26'), ('25.5', '25.5'),
        ('25', '25')], 'PDL')
    pdr = fields.Selection(
        [('40', '40'), ('39.5', '39.5'), ('39', '39'), ('38.5', '38.5'), ('38', '38'), ('37.5', '37.5'), ('37', '37'), ('36.5', '36.5'), ('36', '36'), ('35.5', '35.5'),
        ('35', '35'), ('34.5', '34.5'), ('34', '34'), ('33.5', '33.5'), ('33', '33'), ('32.5', '32.5'), ('32', '32'), ('31.5', '31.5'), ('31', '31'), ('30.5', '30.5'),
        ('20', '20'), ('29.5', '29.5'), ('29', '29'), ('28.5', '28.5'), ('28', '28'), ('27.5', '27.5'), ('27', '27'), ('26.5', '26.5'), ('26', '26'), ('25.5', '25.5'),
        ('25', '25')], 'PDR')

    # pdl = fields.Selection(
    #     [
    #         ('25', '25'), ('25.5', '25.5'), ('26', '26'), ('26.5', '26.5'), ('27', '27'),
    #         ('27.5', '27.5'),
    #         ('28', '28'), ('28.5', '28.5'), ('29', '29'), ('29.5', '29.5'),
    #         ('30', '30'), ('30.5', '30.5'), ('31', '31'), ('31.5', '31.5'), ('32', '32'),
    #         ('32.5', '32.5'),
    #         ('33', '33'), ('33.5', '33.5'), ('34', '34'), ('34.5', '34.5'), ('35', '35'),
    #         ('35.5', '35.5'), ('36', '36'), ('36.5', '36.5'), ('37', '37'), ('37.5', '37.5'),
    #         ('38', '38'), ('38.5', '38.5'), ('39', '39'),
    #         ('39.5', '39.5'), ('40', '40')
    #
    #
    #      ],default='25')
    # pdr = fields.Selection(
    #     [
    #         ('25', '25'), ('25.5', '25.5'), ('26', '26'),('26.5', '26.5'), ('27', '27'),('27.5', '27.5'),
    #         ('28', '28'),('28.5', '28.5'),('29', '29'),('29.5', '29.5'),
    #         ('30', '30'),('30.5', '30.5'), ('31', '31'),('31.5', '31.5'), ('32', '32'),
    #         ('32.5', '32.5'),
    #         ('33', '33'),('33.5','33.5'), ('34', '34'),('34.5', '34.5'), ('35', '35'),('35.5', '35.5'), ('36', '36'),('36.5', '36.5'), ('37', '37'),('37.5', '37.5'),('38','38'),('38.5','38.5'), ('39','39'),
    #         ('39.5','39.5'),('40','40')
    #
    #
    #      ],default='25')
    # Not required
    # prism = fields.Boolean('Prism')
    # prisml = fields.Float('Prism')
    # dim = fields.Float('Dim')
    # diml = fields.Float('Dim')
    # height = fields.Float('Height')
    # heightl = fields.Float('Height')
    # basel = fields.Selection(
    #     [('Select', 'Select'), ('IN', 'IN'), ('OUT', 'OUT'), ('UP', 'UP'), ('DOWN', 'DOWN'),
    #      ], 'basel')
    # prism_vall = fields.Selection(
    #     [('0.25', '0.25'), ('0.5', '0.5'), ('0.75', '0.75'), ('1', '1'),
    #      ('1.25', '1.25'), ('1.5', '1.5'),
    #      ('1.75', '1.75'), ('2', '2'), ('2.25', '2.25'), ('2.5', '2.5'), ('2.75', '2.75'),
    #      ('3', '3'), ('3.25', '3.25'), ('3.5', '3.5'), ('3.75', '3.75'), ('4', '4'), ('4.25', '4.25'),
    #      ('4.5', '4.5'), ('4.75', '4.75'),
    #      ('5', '5')], 'PrismL')
    # lpd = fields.Float('lpd')
    # lpdl = fields.Float('lpd')
    # dual_pd = fields.Boolean('I have Dual PD')
    # pd_distance = fields.Selection(
    #     [('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'),
    #      ('60', '60'), ('70', '70')
    #         , ('79', '79')], 'PD')
    # pd_near = fields.Selection(
    #     [('47', '47'), ('48', '48'), ('49', '49'), ('50', '50'),
    #      ('60', '60'), ('70', '70')
    #         , ('79', '79')], 'PD')

    dr_notes = fields.Text('Notes')
    name = fields.Char(required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
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
