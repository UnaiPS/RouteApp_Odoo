from odoo import models, fields

class Direction(models.Model):
    _name = 'routes.direction'
    
    name = fields.Char()
    country = fields.Char()
    state = fields.Char()
    city = fields.Char()
    district = fields.Char()
    street = fields.Char()
    house_number = fields.Char()
    postal_code = fields.Char()