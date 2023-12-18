from odoo import models, fields, api


class CustomerInvoices(models.Model):
    _name = 'customer.invoices'
    _description = 'Customer invoice'

    name = fields.Many2one('customer.customer', string="Customer Name")
    # name = fields.Char(string="Customer Name")
    date_of_invoice = fields.Date("Invoice Date")
    customer_invoice_number = fields.Char(string='Customer Invoice Id', readonly=True)
    payment_status = fields.Boolean(string="Payment Completed?")



    # for update invoice through the create method
    # name = fields.Char(string="First Name")

    property_name = fields.Selection(
        [('office_space', 'OFFICE SPACE'), ('land', 'LAND'), ('event', 'Event'), ('pg_rooms', 'PG ROOMS'),
         ('appartments', 'Appartments')], string="Property")

    duration_of_stay = fields.Float(string="Duration")

    rent_charges = fields.Float(string="Rent Charges")

    @api.model
    def create(self, vals):
        vals['customer_invoice_number'] = self.env['ir.sequence'].next_by_code('customer.invoice.id')
        return super(CustomerInvoices, self).create(vals)
