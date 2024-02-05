from odoo import models, fields, api
from datetime import date


class CustomerInvoices(models.Model):
    _name = 'customer.invoices'
    _description = 'Customer invoice'

    # name = fields.Char(string="Customer Name")
    date_of_invoice = fields.Date("Invoice Date")
    customer_invoice_number = fields.Char(string='Customer Invoice Id', readonly=True)
    payment_status = fields.Boolean(string="Payment Completed?")

    # for update invoice through the create method
    name = fields.Char(string="Customer Name")

    property_name = fields.Selection([('office_space', 'OFFICE SPACE'),
                                      ('land', 'LAND'),
                                      ('event', 'Event'),
                                      ('pg_rooms', 'PG ROOMS'),
                                      ('appartments', 'Appartments')],
                                     string="Property")

    duration_of_stay = fields.Float(string="Duration")
    start_date = fields.Date(string="Invoice Date")
    end_date = fields.Date(string="End Date")
    rent_charges = fields.Float(string="Rent Charges")
    total_amount = fields.Char(string="Total Amount")
    email = fields.Char(string='Email')

    @api.model
    def create(self, vals):
        vals['customer_invoice_number'] = self.env['ir.sequence'].next_by_code('customer.invoice.id')
        return super(CustomerInvoices, self).create(vals)

    # send by email method on click
    def send_by_email(self):

        reminder_template = self.env.ref('Property_rental.rental_invoice_email')
        escalation_template = self.env.ref('Property_rental.rental_invoice_escalation_email')
        print(self.search([]), "=========")
        customer_data = self.search([])
        for rec in customer_data:
            print(rec, '--------------')
            reminder_mail_date = rec.end_date.day - 1
            escalation_date = rec.end_date.day + 1
            print(reminder_mail_date, '************')

            if date.today().day == reminder_mail_date:
                print('Reminder Email-------------------')
                reminder_template.send_mail(rec.id, force_send=True)
            elif date.today().day == escalation_date:
                print('Escalation Email------------------')
                escalation_template.send_mail(rec.id, force_send=True)
