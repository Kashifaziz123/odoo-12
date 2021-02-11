# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class Attachment(models.Model):
    _inherit = 'ir.attachment'

    def get_file_name_res_id(self,model_char,field_name_char,res_id):
        record = self.env['ir.attachment'].sudo().search([('res_model', '=', model_char),
                                                          ('res_field', '=', field_name_char),
                                                          ('res_id', '=', res_id)], order='id DESC', limit=1)
        return record.store_fname if record else None

    def return_image_url(self,host_name,fname):
        # host name is like https://abc.com/db_directory_name
        # db_directory_name because file folder on lower level so specify in nginx parent directory of folder
       #like filestore/directory with database name
        return host_name + fname


# code is basic but we have mentioned our configuration setps in README.rst

# its important attachment=True when you want to store image in filestore of odoo otherwise it will not create
# not create entry for ir.attachment
title_image = fields.Binary(attachment=True,string='Title Image')