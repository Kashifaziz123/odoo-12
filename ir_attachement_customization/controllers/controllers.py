# -*- coding: utf-8 -*-
from odoo import http

# class LmsProgramPeos(http.Controller):
#     @http.route('/lms_program_peos/lms_program_peos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_program_peos/lms_program_peos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_program_peos.listing', {
#             'root': '/lms_program_peos/lms_program_peos',
#             'objects': http.request.env['lms_program_peos.lms_program_peos'].search([]),
#         })

#     @http.route('/lms_program_peos/lms_program_peos/objects/<model("lms_program_peos.lms_program_peos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_program_peos.object', {
#             'object': obj
#         })