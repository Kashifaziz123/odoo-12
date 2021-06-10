# -*- coding: utf-8 -*-

from odoo import models, fields, api, _,tools
from odoo.exceptions import ValidationError,UserError
from datetime import datetime, timedelta
from odoo.osv import expression
import base64
from PIL import Image
import io

from odoo import _, api, exceptions, fields, models, modules
import mimetypes
from odoo.tools.mimetypes import guess_mimetype


class res_users(models.Model):
    _inherit = 'res.users'

    def _default_groups(self):
        default_group = self.env.ref('base.group_user', raise_if_not_found=False)
        return default_group

    groups_id = fields.Many2many('res.groups', 'res_groups_users_rel', 'uid', 'gid', string='Groups',default=_default_groups)


    @api.multi
    def name_get(self):
        result = []
        for record in self:
            faculty = self.env['ums.faculty'].sudo().get_faculyobj_by_currentuser(record.id)
            student = self.env['ums.student'].sudo().search([('user_id', '=', record.id)])
            if faculty and record.partner_id:
                name = faculty.faculty_id + '-' + str(record.name)
            elif student and record.is_student:
                name = student.student_id + '-' + str(record.name)
            elif record.is_external:
                name = str(record.name) + '-' + str(record.email)
            else:
                name = record.name
            result.append((record.id, name))
        return result

    @api.onchange('image')
    def image_onchange(self):
        if self.image:
            image_path = self.image
            imgdata = base64.b64decode(str(image_path))
            image = Image.open(io.BytesIO(imgdata))
            new_image = image.convert("RGB")
            new_image.thumbnail((900, 900))
            buffered = io.BytesIO()
            new_image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue())
            self.image = img_str
            lecturer = self.env['ums.faculty'].sudo().search([('user_id', '=', self.id)], limit=1)
            student = self.env['ums.student'].search([('user_id', '=', self.id)])
            if lecturer:
                self.env['ums.faculty'].sudo().browse(lecturer.id).write({'image': img_str})
            if student:
                self.env['ums.student'].sudo().browse(student.id).write({'image': img_str})





