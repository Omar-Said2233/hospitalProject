
from odoo import models, fields, api

class MyOrder(models.Model):
    _name = 'my.order'

    name = fields.Char()
    item_ids = fields.One2many('my.order.item','order_id')

    def action(self):
        self.env['my.order.item'].create({
            'name': 'Ahmed',
            'price': 15.5,
            'order_id': self.id

        })

        
class MyOrderItem(models.Model):
    _name = 'my.order.item'

    name = fields.Char()
    Date = fields.Date()
    price = fields.Float()
    order_id = fields.Many2one('my.order')
