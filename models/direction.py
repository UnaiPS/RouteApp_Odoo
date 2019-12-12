from odoo import models, fields, api

class Direction(models.Model):
    _name = 'routes.direction'
    
    direction_id = field.Integer()
    name = field.Char()
    country = field.Char()
    state = field.Char()
    city = field.Char()
    district = field.Char()
    street = field.Char()
    house_number = field.Char()
    postal_code = field.Char()