from odoo import models, fields
from odoo.addons import base

class my_module(models.Model):
    _inherit = 'res.users'
    employee_id = fields.Char(String="Employee ID")




