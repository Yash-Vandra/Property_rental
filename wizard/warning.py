from odoo import models, fields, api


class WarningWizard(models.TransientModel):
    _name = 'warning.wizard'

    warning = fields.Char(string="Warning", default='This Property Already On Rent')

    # force-fully assign button
    # @api.model
    # def default_get(self, fields_list):
    #     print('selfffffffffffffffffffff', self)
    #     print('fieldddddddddddddddd', fields_list)
    #     record = self.env['customer.office.data'].browse(self.env.context.get('active_ids'))
    #     print(record.id, 'recorddddddd')
    #     print(record.customers, 'prrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    #     res = super(WarningWizard, self).default_get(fields_list)
    #
    #     print('resssssssssssssssssssssssss', res)
    #     return res

    def forcefully_assign_button(self):
        context = self.env.context
        # print(type(context.get('customer')),'____________________________________-',context.get('customer'))
        customer_name = self.env['customer.customer'].browse([context.get('customer')])

        customer_record = self.env['customer.customer'].search([])
        record = self.env['property.list'].browse(self.env.context.get('ids'))
        store_rec = []
        customer_id = []
        for rec in customer_record:
            for res in record:
                if res in (rec.property_list):
                    store_rec.append(res)
                    customer_id.append(rec)

        for cust in customer_id:
            for prop in store_rec:
                cust.update({
                    'property_list': [(fields.Command.unlink(prop.id))]
                })
        customer_name.update({
            'property_list': [(fields.Command.set(self.env.context.get('ids')))]
        })
        # customer = self.env['customer.customer'].browse(context.get('customer'))
        # customer.update({
        #     'property_list': [(fields.Command.set(self.env.context.get('ids')))]
        # })
        #
        # record_set = self.env['customer.office.data'].browse(self.env.context.get('active_ids'))
        # customer_record = self.env['customer.customer'].search([])

        # for rec in customer_record:
        #     print(rec,'Recccccccc')
        #     print(rec.id,'Recccccccc iddddddd')
        #     for res in self.env.context.get('ids'):
        #         print(res,'ressssssssss')
        #         print(self.env.context.get('ids'),'+++++++')
        #         if str(res) in str(rec.id) :
        #             customer.update({
        #                 'property_list': [(fields.Command.unlink(rec.id))]
        #             })
        #         else:
        #             print('NOOOOOOO')
