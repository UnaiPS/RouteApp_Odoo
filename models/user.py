from odoo import models, fields

class User(models.Model):
    _inherit ='res.user'
    admin = fields.Boolean("Admin", default=False)
    
