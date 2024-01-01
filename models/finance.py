from odoo import models, fields,api


class Finance(models.Model):
    _name = 'finance.finance'
    _description = 'Finance Details'

    name = fields.Char(string="Company name", default='Rental Services Pvt.Ltd')
    property_services_list =  fields.Selection([('office_space', 'OFFICE SPACE'),
                                      ('land', 'LAND'),
                                      ('event', 'Event'),
                                      ('pg_rooms', 'PG ROOMS'),
                                      ('appartments', 'Appartments'),
                                      ('all','All')],
                                     string="Property List")
    per_quarter = fields.Selection([('first_quarter', 'First Quarter'),
                                    ('second_quarter', 'Second Quarter'),
                                    ('third_quarter', 'Third Quarter'),
                                    ('fourth_quarter', 'Fourth Quarter')]
                                   , string='Quarter')

    per_property_income = fields.Char(string='Property Income')
    total_income = fields.Char(string='Total Amount')

    @api.onchange('property_services_list')
    def sum_office_space(self):
        total_income_per_property = 0
        income_per_property = self.env['customer.invoices'].search([('property_name','=',self.property_services_list)])
        # print(income_per_property,'----------------------------------')
        for rec in income_per_property:
            # print('-----------------------------',rec)
            total_income_per_property += float(rec.total_amount)
        self.per_property_income = total_income_per_property

        if self.property_services_list == 'all':
            generation_of_income =0
            total_generation_ofincome = self.env['customer.invoices'].search_read([],fields=['total_amount'])
            # print(total_generation_ofincome,'______________________*')
            for record in total_generation_ofincome:
                (generation_of_income) = float(generation_of_income) + float(record['total_amount'])
                self.total_income = generation_of_income



