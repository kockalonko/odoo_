# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class c:\odoo\comunity\odoo\addons(models.Model):
#     _name = 'c:\odoo\comunity\odoo\addons.c:\odoo\comunity\odoo\addons'
#     _description = 'c:\odoo\comunity\odoo\addons.c:\odoo\comunity\odoo\addons'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
