from odoo import models, fields, api
from odoo.addons import base

class my_module(models.Model):
    _inherit = 'res.users'
    count_login = fields.Integer(string='Count login')


def count_login_record(self, login):
    count_login = self.env['res.user'].search_count([('login', '=', login)])
    return count_login