# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/customModule(http.Controller):
#     @http.route('//mnt/extra-addons/custom_module//mnt/extra-addons/custom_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/custom_module//mnt/extra-addons/custom_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/custom_module.listing', {
#             'root': '//mnt/extra-addons/custom_module//mnt/extra-addons/custom_module',
#             'objects': http.request.env['/mnt/extra-addons/custom_module./mnt/extra-addons/custom_module'].search([]),
#         })

#     @http.route('//mnt/extra-addons/custom_module//mnt/extra-addons/custom_module/objects/<model("/mnt/extra-addons/custom_module./mnt/extra-addons/custom_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/custom_module.object', {
#             'object': obj
#         })
