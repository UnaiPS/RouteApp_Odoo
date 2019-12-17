from openerp import models, fields
class Route(models.Model):
    _name = 'routes.route'
    name = fields.Char(required=True)
    origin_id = fields.Many2one('routes.direction',ondelete='cascade', string="Origin", required=True)
    destination_ids = fields.Many2many('routes.direction', string="Destinations", required=True)
    worker_id = fields.Many2one('routes.routeuser',ondelete='cascade', string="Assigned to", required=True)
    author_id = fields.Many2one('routes.routeuser',ondelete='cascade', string="Created by", required=True)
    product_ids = fields.Many2many('product.product', string="Product/Service", required=True)
    distance = fields.Float()
    time = fields.Float()
    completed = fields.Boolean("Completed", default=False, required=True)


    
