from odoo import models, fields

class Routeuser(models.Model):
    _name = 'routes.routeuser'
    _inherit ='res.users'
    admin = fields.Boolean("Admin", default=False)
    
