from odoo import models, fields, api


class OfficeSpace(models.Model):
    _name = 'office.space'
    _description = "Services That Provided"

    # name = fields.Many2one('customer.customer',string="Customer Name")
    name = fields.Char(string="Customer Name")
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

    image_office = fields.Binary(string='IMG')

    # server action of office allocation
    def office_space_allocation(self):
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
    # wizard onchange on customer


