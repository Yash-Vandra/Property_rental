from odoo import models,fields,api
from datetime import date,datetime

class Customer(models.Model):
    _name = 'customer.customer'
    _description = "Customer Data"

    name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email Id",required=True)
    phone = fields.Char(string="Phone")
    documents = fields.Binary(string="Documents" , required=True)
    property_name = fields.Selection([('office_space','OFFICE SPACE'),('land','LAND'),('event','Event'),('pg_rooms','PG ROOMS'),('appartments','Appartments')],string="Property",required=True)
    charges_paid  = fields.Float(string='Charges Paid ', required=True)
    start_date = fields.Date(string="Date")
    end_date = fields.Date(string="End Date")
    duration_of_stay = fields.Float(string="Duration")

    rent_agreement_copy = fields.Binary("Rent Agreement",required=True)

    def customer_preview(self):
        print("Clicked..................................")

    @api.onchange('start_date','end_date')
    def onchange_duration(self):
        if self.start_date:
            if self.end_date:
                self.duration_of_stay =self.end_date.year-self.start_date.year




