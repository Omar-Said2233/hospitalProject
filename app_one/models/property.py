from logging import warning

from reportlab.lib.validators import inherit

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError
from odoo.odoo.tools.populate import compute


class Property(models.Model):
    _name = 'property'
    inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=True, default="new", size=12)
    description = fields.Text()
    postcode = fields.Char()
    diff = fields.Float(compute='_compute_diff')
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float(required=True)
    bedrooms = fields.Integer(required=True)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ])
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
        ('sold','Sold'),
        ('closed','Closed'),
    ])
    owner_address = fields.Char(related='owner_id.address',readonly=0)
    owner_phone = fields.Char(related='owner_id.phone',readonly=0)

    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')

    line_ids = fields.One2many('property.line','property_id')

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This Name is Exist!')
    ]
    @api.depends('expected_price','selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price + rec.selling_price

    @api.onchange('selling_price')
    def _onchange_selling_price(self):
        for rec in self:
            return {
                'warning':{'title':'warning','message':'خطأ في القيمة' , 'type':'notification'}
            }

    @api.constrains('selling_price')
    def _check_selling_price(self):
        for rec in self:
            if rec.selling_price == 0:
                raise ValidationError('please inter selling price ')

    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([('name', '=', record.name)]) > 1:
                raise ValidationError("The name must be unique!")

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print("hello")
    #     return res

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            rec.state = 'closed'

class PropertyLine(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property')
    area = fields.Float()
    discription = fields.Char()