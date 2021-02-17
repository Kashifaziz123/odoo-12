# -*- coding: utf-8 -*-
from odoo import http

# class UmsClass(http.Controller):
#     @http.route('/ums_class/ums_class/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ums_class/ums_class/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ums_class.listing', {
#             'root': '/ums_class/ums_class',
#             'objects': http.request.env['ums_class.ums_class'].search([]),
#         })

#     @http.route('/ums_class/ums_class/objects/<model("ums_class.ums_class"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ums_class.object', {
#             'object': obj
#         })