from odoo import models, fields


class Broker(models.Model):
    _name = 'broker.broker'
    _description = 'Broker data'

    name = fields.Char(string="Name")
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    broker_license = fields.Binary(string='Broker Licence')
    identity_proof = fields.Selection([('aadhar', 'Aadhar Card'),
                                       ('pan', 'Pan Card'),
                                       ('voter_id', 'Voter Id'),
                                       ('driving_license', 'Driving License')])
    commission_charges = fields.Char(string="Commission", default="5%")
