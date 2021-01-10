from odoo import api, fields, models,_


class InheritedResPartner(models.Model):
    _inherit = 'res.partner'

    user_active = fields.Boolean()
    related_user = fields.Char()

    def create_users(self):
        self.user_active='True'
        self.related_user=self.name
        vals = {
            'company_id': self.env.ref('base.main_company').id,
            'name': self.name,
            'login':self.name,
            'email': self.email,
            'partner_id':self.id,
            'groups_id': [(6, 0, [self.env.ref('base.group_user').id])]
        }
        users = self.env['res.users'].create(vals)











