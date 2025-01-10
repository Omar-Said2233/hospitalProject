
from odoo import models, fields, api

class ContactNew(models.Model):
    _inherit = 'res.partner'

    my_note = fields.Char()
    my_phone_nubmer = fields.Char()

