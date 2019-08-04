from odoo import api, tools, fields, models, _
import base64
from odoo import modules


class InheritUser(models.Model):
    _inherit = 'pos.config'

    related_pos_user = fields.One2many('pos.session.users', 'pos_config', string='Related User')


class InheritSession(models.Model):
    _name = 'pos.session.users'

    user = fields.Many2one('res.users')
    pos_config = fields.Many2one('pos.config')


class InheritUser(models.Model):
    _inherit = 'res.users'

    pos_sessions = fields.Many2many('pos.config', string='Point of Sale Accessible')

    
    @api.multi
    def write(self, vals):
        if 'pos_sessions' in vals:
            if vals['pos_sessions'][0][2]:
                self.env['pos.session.users']
                self.env["pos.session.users"].search(
                    [('user', '=', self.id)]).unlink()
                for pos_session in vals['pos_sessions'][0][2]:
                    self.env['pos.session.users'].create({'pos_config': pos_session, 'user': self.id})
            else:
                self.env["pos.session.users"].search(
                    [('user', '=', self.id)]).unlink()
        result = super(InheritUser, self).write(vals)
        return result

    @api.model
    def create(self, vals):
        create_id = super(InheritUser, self).create(vals)
        if vals['pos_sessions'][0][2]:
            for pos_session in vals['pos_sessions'][0][2]:
                self.env['pos.session.users'].create({'pos_config': pos_session, 'user': create_id.id})
        return create_id
