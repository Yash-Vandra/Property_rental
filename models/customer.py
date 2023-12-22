from odoo import models, fields, api
from datetime import date, datetime


class Customer(models.Model):
    _name = 'customer.customer'
    _description = "Customer Data"

    # _rec_name = 'customer_id'
    name = fields.Char(string="First Name")
    mycompany_name = fields.Char(string="Company Name")
    last_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email Id", required=True)
    phone = fields.Char(string="Phone")
    documents = fields.Binary(string="Documents", required=False)
    property_name = fields.Selection(
        [('office_space', 'OFFICE SPACE'), ('land', 'LAND'), ('event', 'Event'), ('pg_rooms', 'PG ROOMS'),
         ('appartments', 'Appartments')], string="Property", required=True)
    start_date = fields.Date(string="Date")
    end_date = fields.Date(string="End Date")
    duration_of_stay = fields.Float(string="Duration")
    rent_charges = fields.Float(string="Rent Charges")
    rent_agreement_copy = fields.Binary("Rent Agreement", required=False)

    customer_id = fields.Char("Customer Id", readonly=True)

    def customer_preview(self):
        print("Clicked..................................")

    @api.onchange('start_date', 'end_date')
    def onchange_duration(self):
        if self.start_date:
            if self.end_date:
                if self.start_date.year == self.end_date.year:
                    self.duration_of_stay = self.end_date.month - self.start_date.month
                else:
                    total_months = (self.end_date.year - self.start_date.year) * 12
                    months_to_cut = self.start_date.month - self.end_date.month
                    self.duration_of_stay = total_months - months_to_cut

    # to make/update invoice
    def update_customer_invoice(self):
        print('Invoiced.......................')
        self.env['customer.invoices'].create({
            # 'name':self.name,
            'duration_of_stay': self.duration_of_stay,
            'property_name': self.property_name,
            'rent_charges': self.rent_charges,
        })

    # serial number and company name
    @api.model
    def create(self, vals):
        vals['customer_id'] = self.env['ir.sequence'].next_by_code('customer.unique.id')
        vals['mycompany_name'] = 'Rental Services Pvt.Ltd'
        return super(Customer, self).create(vals)

    def write(self, vals):
        vals['mycompany_name'] = 'Rental Services Pvt.Ltd'
        return super(Customer, self).write(vals)
