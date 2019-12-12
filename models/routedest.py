from openerp import models, fields
class Routedest(models.Model):
    _name = 'routes.routedest'
    _inherits = {
        'routes.direction': 'direction_id'
    }
    
    route_id = fields.Many2one('routes.route', string="Route", required=True)
    product_ids = fields.Many2many('product.product', string="Product/Service", required=True)
    visited = fields.Boolean(required=True)
    