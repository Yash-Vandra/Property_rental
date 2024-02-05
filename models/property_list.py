from odoo import models, fields, api


class PropertyList(models.Model):
    _name = 'property.list'
    _description = "Property List details"

    name = fields.Char(string="Property Name")
    # name_one = fields.Char(string="Customer Name")

    building_area = fields.Float(string="Building area(Sq.ft)")
    age_of_building = fields.Char(string="Age Of Building")
    office_floor = fields.Integer(string="Floor")
    office_address = fields.Text(string="Address")
    office_location = fields.Char(string="Location")

    office_charges_paid = fields.Float(string='Charges Paid ', required=True)
    office_payment_mode = fields.Selection([('cash', 'Cash'),
                                            ('credit_card', 'Credit Card'),
                                            ('debit_card', 'Debit Card'),
                                            ('upi', 'Upi'),
                                            ('internet_banking', 'Internet Banking')],
                                           string='Payment Mode')


    def property_list_allocation(self):
        print('Server action______________________')
        return {
            "name": "Allocated Office",
            "type": "ir.actions.act_window",
            "res_model": "customer.office.data",
            'view_mode': 'form',
            "view_type": "form",
            'target': 'new',
            'view_id': self.env.ref('Property_rental.customer_office_data_wizard_form').id,
        }