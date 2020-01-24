from openerp import models, fields
#from odoo import exceptions

class Route(models.Model):
    _name = 'routes.route'
    name = fields.Char(required=True, default="New Route")
    origin_id = fields.Many2one('routes.direction',ondelete='cascade', string="Origin", required=True)
    destination_ids = fields.Many2many('routes.direction', string="Destinations", required=True)
    worker_id = fields.Many2one('routes.routeuser',ondelete='cascade', string="Assigned to", required=True)
    author_id = fields.Many2one('routes.routeuser',ondelete='cascade', string="Created by", required=True)
    product_ids = fields.Many2many('product.product', string="Product/Service", required=True)
    distance = fields.Float()
    time = fields.Float()
#    speed = fields.Char()
    completed = fields.Boolean("Completed", default=False, required=True)

#@api.constrains('origin_id', 'destination_ids')
#def _check_origin_not_destination(self):
#    for r in self:
#        if r.origin_id and r.origin_id in r.destination_ids:
#            raise exceptions.Warning("A route's origin cannot be a destination")

#@api.onchange('distance', 'time')
#def _onchange_speed:
#    if self.distance / self.time >= 0.7 and self.distance / self.time <= 1.25:
#        self.speed = "normal"
#    elif self.distance / self.time < 0.7:
#        self.speed = "slow"
#    else:
#        self.speed = "fast"