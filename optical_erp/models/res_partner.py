from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models,_

class InheritedResPartner(models.Model):
    _inherit = 'res.partner'

    dob = fields.Date()
    age = fields.Integer(compute='_cal_age',store=True,readonly=True)

    @api.depends('dob')
    def _cal_age(self):
        for record in self:
            if record.dob:
                years = relativedelta(date.today(), record.dob).years
                record.age = str(int(years))
            else:
                record.age = 0














