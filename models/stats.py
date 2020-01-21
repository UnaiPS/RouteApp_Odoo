from odoo import models, fields

class Stats(models.Model):
    _name = 'routes.stats'
    name = fields.Char()