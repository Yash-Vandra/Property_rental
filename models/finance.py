from odoo import models, fields


class Finance(models.Model):
    _name = 'finance.finance'
    _description = 'Finance Details'

    name = fields.Char(string="Company name", default='Rental Services Pvt.Ltd')
    property_services_list = fields.Selection([('office', 'Office'),
                                               ('land', 'Land'),
                                               ('pg', 'PGs'),
                                               ('appartment', 'Appartment'),
                                               ('event', 'Event')],
                                              string='Property List')
    per_quarter = fields.Selection([('first_quarter', 'First Quarter'),
                                    ('second_quarter', 'Second Quarter'),
                                    ('third_quarter', 'Third Quarter'),
                                    ('fourth_quarter', 'Fourth Quarter')]
                                   , string='Quarter')

    per_property_income = fields.Char(string='Property Income', compute='_compute_per_property_income')

    total_income = fields.Char(string='Total Amount')

    # compute for the property income

    def _compute_per_property_income(self):
        for rec in self:
            print()
