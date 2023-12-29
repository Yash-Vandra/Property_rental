from odoo import models, fields


class Appartment(models.Model):
    _name = 'appartment.appartment'
    _description = "Appartment Provided"

    # name = fields.Many2one('customer.customer', string="Customer Name")
    name = fields.Char(string="Customer Name")

    carpet_area = fields.Integer("Carpet Area")
    available_for = fields.Selection([('boys', 'Boys'),
                                      ('girls', 'Girls'),
                                      ('family', 'Family')])
    deposit_amount = fields.Integer("Security Deposit")
    house_type = fields.Selection([('1bhk', '1 BHK'),
                                   ('2bhk', '2 BHk'),
                                   ('3bhk', '3 BHk'),
                                   ('4bhk', '4 BHK')])
    appartment_ac_nonac = fields.Selection([('ac', 'Ac'),
                                            ('non_ac', 'Non Ac')],
                                           string="Ac/Non-Ac")
    appartment_locality = fields.Selection([('vastapur', 'Vastrapur'),
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
    appartment_parking = fields.Boolean("Parking")
    charges_paid = fields.Float(string='Charges Paid ', required=True)

    appartment_img = fields.Char("Img")
