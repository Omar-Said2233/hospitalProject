from gevent.win32util import formatError

from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'

    ref = fields.Char(default = 'New', readonly=1)
    name = fields.Char('Task Name')
    due_data = fields.Date()
    description = fields.Text()
    assign_to_id = fields.Many2one('res.partner')
    state = fields.Selection([
        ('new','New'),
        ('old','Old'),
        ('and','And'),
    ], default='old')

    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_old(self):
        for rec in self:
            rec.state = 'old'

    def action_new_and(self):
        for rec in self:
            rec.state = 'new_and'

    def action(self):
        print(self.env.user.name)

    @api.model
    def create(self, vals):
        res = super(TodoTask,self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('todo_sequence')
        return res

