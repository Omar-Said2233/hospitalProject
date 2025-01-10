# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class MySchool(models.Model):
     _name = 'my.school'
     _description = 'my_school'
     _inherit = ['mail.thread', 'mail.activity.mixin']

     name = fields.Char(tracking=True)
     value = fields.Integer()
     value2 = fields.Float()
     description = fields.Text()
     trueFalse = fields.Boolean()
     html = fields.Html()
     data = fields.Date()
     data_time = fields.Datetime()
     binary = fields.Binary()
     select = fields.Selection([
         ('1','Vall1'),
         ('2','Vall2'),
         ('3','Vall3'),
     ])
     state = fields.Selection([
         ('new','New'),
         ('used','Used'),
         ('old','Old'),
         ('expired','Expired')
     ], string='Status', requied=True, default='new')

     def button_in_used(self):
         for course in self:
             course.write({'state' : 'used'})

     def button_in_old(self):
         for course in self:
             course.write({'state' : 'old'})

     def button_in_expied(self):
         for course in self:
             course.write({'state' : 'expired'})

     def button_in_new(self):
         for course in self:
             course.write({'state' : 'new'})


     call1 = fields.Float(string='Vall 1')
     call2 = fields.Float(string='Vall 2')
     result = fields.Float(string = 'vall 1 + vall 2', readonly='1')

     computed = fields.Float(compute='value_pc', store=1)

     def action(self):
         print(self.env)

     def event_used(self):
         self.status = 'used'

     @api.constrains('value')
     def _check_age(self):
         if self.value <= 26 or self.value >= 35:
             raise ValidationError(_('age must between 25 and 35'))

     @api.depends('result')
     def value_pc(self):
         for record in self:
             record.computed = record.result * 10

     @api.onchange('call1','call2')
     def on_change_value(self):
         self.result = self.call1 + self.call2



    #
    # _sql_constraints = [
    #     ('uniq_name', 'UNIQUE("name")', 'this name is already hear')
    # ]
    #

