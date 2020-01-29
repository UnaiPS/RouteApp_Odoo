from odoo import models, fields

class Routeuser(models.Model):
    _name = 'routes.routeuser'
    _inherit ='res.user'
    route_id = fields.One2many('routes.route', string="route")
    admin = fields.Boolean("Admin", default=False)
    