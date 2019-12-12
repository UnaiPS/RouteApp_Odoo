from openerp import models, fields
class Route(models.Model):
    _name = 'routes.route'
    name = field.Char(required=True)
    origin_id = fields.Many2one('routes.direction',ondelete='cascade', string="Origin", required=True)
    destination_ids = fields.One2many('routes.routedest', string="Destinations", required=True)
    worker_id = fields.Many2one('routes.user',ondelete='cascade', string="Assigned to", required=True)
    author_id = fields.Many2one('routes.user',ondelete='cascade', string="Created by", required=True)
    distance = fields.Float()
    time = fields.Float()


    
