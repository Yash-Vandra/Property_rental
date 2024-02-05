from odoo import models, fields, api


class CustomerOfficeWizard(models.TransientModel):
    _name = 'customer.office.data'

    customers = fields.Many2one(comodel_name='customer.customer', string='Customers')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    @api.onchange('customers')
    def onchange_customers(self):
        print('-------------------------------------------')
        self.phone = self.customers.phone
        self.email = self.customers.email

    # assign button
    def assign_button(self):
        # print('++++++++++')
        customer_record = self.env['customer.customer'].search([])
        record = self.env['property.list'].browse(self.env.context.get('active_ids'))
        store_rec = []
        print('PRO.................',self.env.context.get('active_ids'))
        for rec in customer_record:
            print(rec, '======RECCC============')
            for res in record:
                print(res,'++++++++++++ressssssssss+++++++++++++++++')
                if res in (rec.property_list):
                    print(res , '---------RESSSSS----------')
                    store_rec.append(res)
                    print(store_rec.append(res),'-------PRINT---------')
                else:
                    print('PROPERTY NATHI APEL.................')
        if store_rec == []:
            print("OFFICE KHALI CHE")
            self.customers.update({
                'property_list': [(fields.Command.set(self.env.context.get('active_ids')))]
            })
        else:
            print('PROPERTY APEL CHEE')
            return {
                "name": "Warning/Assign wizard",
                "type": "ir.actions.act_window",
                "res_model": "warning.wizard",
                'view_mode': 'form',
                "view_type": "form",
                'target': 'new',
                'view_id': self.env.ref('Property_rental.warning_wizard_form').id,
                'context': {'customer': self.customers.id, 'ids': self.env.context.get('active_ids')}
            }


