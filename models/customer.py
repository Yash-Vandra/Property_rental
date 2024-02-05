from odoo import models, fields, api
from datetime import date, datetime
from odoo.exceptions import ValidationError


class Customer(models.Model):
    _name = 'customer.customer'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer Data"

    # _rec_name = 'customer_id'
    name = fields.Char(string="First Name")
    mycompany_name = fields.Char(string="Company Name", readonly=True)
    last_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email Id", required=True)
    phone = fields.Char(string="Phone")
    documents = fields.Binary(string="Documents", required=False)
    property_name = fields.Selection([('office_space', 'Office Space'),
                                      ('land', 'Land'),
                                      ('event', 'Event'),
                                      ('pg_rooms', 'Pg Rooms'),
                                      ('appartments', 'Appartments')],
                                     string="Property",
                                     required=True)
    start_date = fields.Date(string="Start Date", default=datetime.now())
    end_date = fields.Date(string="End Date")
    duration_of_stay = fields.Float(string="Duration")
    rent_charges = fields.Float(string="Rent Charges", tracking=True)
    rent_agreement_copy = fields.Binary("Rent Agreement", required=False)
    customer_id = fields.Char("Customer Id", readonly=True)
    total_amount = fields.Char(string="Total Amount", store=True)

    property_list = fields.Many2many('property.list',string='Property List')

    @api.onchange('duration_of_stay', 'rent_charges')
    def onchange_total_amount(self):
        self.total_amount = self.duration_of_stay * self.rent_charges

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
            'name': self.name,
            'duration_of_stay': self.duration_of_stay,
            'property_name': self.property_name,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'rent_charges': self.rent_charges,
            'total_amount': self.total_amount,
            'email': self.email,
        })

    # to update services
    def update_services(self):
        print('Updated Services.......................')
        if self.property_name == 'office_space':
            print('**__**--**')
            self.env['office.space'].create({
                'name': self.name,
                'office_charges_paid': self.rent_charges,
            })
        elif self.property_name == 'land':
            self.env['land.land'].create({
                # 'name': self.name,
                'land_charges_paid': self.rent_charges,
            })
        elif self.property_name == 'pg_rooms':
            self.env['pg.rooms'].create({
                # 'name': self.name,
                'pg_charges_paid': self.rent_charges,
            })

        elif self.property_name == 'appartments':
            self.env['appartment.appartment'].create({
                # 'name': self.name,
                'charges_paid': self.rent_charges,
            })
        elif self.property_name == 'event':
            self.env['event.event'].create({
                # 'name': self.name,
                'event_charges_paid': self.rent_charges,
            })
        else:
            print('Select Property Name ')

    # serial number and company name
    @api.model
    def create(self, vals):
        vals['customer_id'] = self.env['ir.sequence'].next_by_code('customer.unique.id')
        vals['mycompany_name'] = 'Rental Services Pvt.Ltd'
        return super(Customer, self).create(vals)

    def write(self, vals):
        vals['mycompany_name'] = 'Rental Services Pvt.Ltd'

        from_property = dict(self._fields['property_name'].selection)
        if 'property_name' in vals:
            self.message_post(body=f"Changed From {from_property[self.property_name]} To {from_property[vals['property_name']]}")

        return super(Customer, self).write(vals)

    # unlink method for if customer records deleted , it stores in the customer invoices
    def unlink(self):
        self.env['customer.invoices'].create({
            'name': self.name,
            'duration_of_stay': self.duration_of_stay,
            'property_name': self.property_name,
            'start_date': self.start_date,
            'rent_charges': self.rent_charges,
            'total_amount': self.total_amount,
        })

        rtn = super(Customer, self).unlink()
        print('--------------->', rtn)
        return rtn

    # for email constraints

    @api.constrains('email')
    def _constrains_email(self):
        for rec in self:
            email = self.search([('email', '=', rec.email), ('id', '!=', rec.id)])
            print('emailllllllllllllllllll', email)
            if email:
                raise ValidationError('Mail : %s is already taken' % rec.email)

    # @api.onchange('property_name')
    # def _track_subtype(self, init_values):
    #     print(init_values, '______________________________________________')
    #     v = self.ensure_one()
    #     print(v, '<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>,.')
    #     if 'property_name' in init_values:
    #         return self.env.ref('Property_rental.rental_customer_form')
    #     return super(Customer,self)._track_subtype(init_values)

    # oe chatter button
    def click_oe_chatter(self):
        self.message_post(body='Hello')

    # message post in chatter

