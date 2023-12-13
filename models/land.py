from odoo import models,fields

class Land(models.Model):
    _name = 'land.land'
    _description = "Land details"

    name = fields.Many2one('customer.customer',string="Customer Name")

    plot_area = fields.Float(string="Plot Area(Sq.ft)")
    dimensions = fields.Char(string="Dimensions(L x B)")
    direction_faced = fields.Char(string="Facing")
    land_rent = fields.Float(string="Rent")
    land_img = fields.Char(string="IMG")


