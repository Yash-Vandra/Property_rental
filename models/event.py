from odoo import models, fields


class Event(models.Model):
    _name = 'event.event'
    _description = "rental proprety for the event"

    # name = fields.Many2one('customer.customer', string="Customer Name")
    name = fields.Char(string="Customer Name",required=True)
    event_name = fields.Selection([('wedding', 'Wedding'),
                                   ('birthday', 'Birthday Party'),
                                   ('babyshower', 'Baby Shower'),
                                   ('coorporate event', 'Coorporate Events'),
                                   ('sangeet ceremony', 'Sangeet Ceremony'),
                                   ('workshop', 'Workshops')])
    mode_of_payment = fields.Selection([('cash', 'Cash'),
                                        ('credit_card', 'Credit Card'),
                                        ('debit_card', 'Debit Card'),
                                        ('upi', 'Upi'),
                                        ('internet_banking', 'Internet Banking')])
    seating_capacity = fields.Char(string="Seating Capacity")
    event_address = fields.Char(string="Address")
    event_charges_paid = fields.Integer("Charges Paid", required=True)
    event_img = fields.Char(string="Img")
