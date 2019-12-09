# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Worker(models.Model):
        _name = 'routes.worker'
        
        name = fields.Char(required=True)
        email = fields.Char(required=True)
        routes_id = fields.One2many('routes.route', 'route_id', string="Routes")
