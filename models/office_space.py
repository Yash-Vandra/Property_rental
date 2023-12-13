from odoo import models,fields

class OfficeSpace(models.Model):
    _name = 'office.office'
    _description = "Services That Provided"

    name = fields.Many2one('customer.customer',string="Customer Name")

    building_area = fields.Float(string="Building area(Sq.ft)")
    age_of_building = fields.Char(string="Age Of Building")
    office_floor = fields.Integer(string="Floor")
    office_address = fields.Text(string="Address")
    office_location = fields.Char(string="Location")
    office_rent = fields.Float(string='Rent')
    image_office = fields.Char(string='IMG')


