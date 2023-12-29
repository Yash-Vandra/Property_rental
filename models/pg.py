from odoo import models, fields


class Pgrooms(models.Model):
    _name = 'pg.rooms'
    _description = "Pg rooms Provided"

    # name = fields.Many2one('customer.customer', string="Customer Name")
    name = fields.Char(string="Customer Name")
    available_for = fields.Selection([('boys', 'Boys'), ('girls', 'Girls'), ('family', 'Family')])
    deposit_amount = fields.Integer("Deposit")
    room_type = fields.Selection([('single', 'Single Sharing'),
                                  ('double', 'Double Sharing'),
                                  ('tripe', 'Triple Sharing'),
                                  ('four', 'Four Sharing'),
                                  ('six', 'Six Sharing')])
    ac_nonac = fields.Selection([('ac', 'Ac'),
                                 ('non_ac', 'Non Ac')],
                                string="Ac/Non-Ac")
    locality = fields.Selection([('vastapur', 'Vastrapur'),
                                 ('ellis_bridge', 'Ellis Bridge'),
                                 ('naranpura', 'Naranpura'),
                                 ('ambawadi', 'Ambawadi'),
                                 ('maninagar', 'Maninagar'),
                                 ('gota', 'Gota'),
                                 ('cg_road', 'CG Road'),
                                 ('chandkheda', 'Chandkheda'),
                                 ('ghatlodiya', 'Ghatlodiya'),
                                 ('chandlodiya', 'Chandlodiya'),
                                 ('thaltej', 'Thaltej'),
                                 ('vatva', 'Vatva')])
    parking = fields.Boolean("Parking")
    pg_charges_paid = fields.Float(string='Charges Paid ', required=True)
    pg_img = fields.Char("Img")
