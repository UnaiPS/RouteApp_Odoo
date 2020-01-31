from odoo import models, fields

class Routeuser(models.Model):
    _inherit ='res.partner'
    created_route_id = fields.One2many('routes.route','author_id', string='Route1')
    assigned_route_id = fields.One2many('routes.route','worker_id', string='Route2')
    admin = fields.Boolean("Admin", default=False)
    
    
    
