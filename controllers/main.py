from odoo import http
from odoo.http import request


class OfficeSpace(http.Controller):
    @http.route(['/officespace/'], type="http", auth="public", website="True")
    def rental_office(self, **post):
        rental_office = request.env['office.space'].sudo().search([])
        print(rental_office, 'reeeeeeeeeentallllllllllll')
        values = {
            'records_rental_office': rental_office
        }

        return request.render("Property_rental.website_officespace", values)


class Customers(http.Controller):
    _inherit = 'res.partner'
    @http.route(['/customer/'], type="http", auth="public", website="True")
    def customer_list(self, **post):
        res_customers = request.env['res.partner'].sudo().search([])
        print(res_customers, 'partnerrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        values = {
            'res_customers': res_customers
        }

        return request.render("Property_rental.website_res_customer", values)

    @http.route(['/customer/views/<int:id>'], type="http", auth="public", website="True")
    def customer_list_view(self,id=None,**post):

        res_customers_view = request.env['res.partner'].sudo().browse([id])
        print(res_customers_view, 'partnerrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
        values = {
            'res_customers_view': res_customers_view
        }

        return request.render("Property_rental.website_res_customer_list", values)
