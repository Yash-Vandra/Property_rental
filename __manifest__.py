{
    'name': "Rental Property",
    'depends':['base','sale_management'],
    'data': [
        'views/menu_views.xml',
        'views/customer_views.xml',
        'views/officespace_views.xml',
        'views/land_views.xml',
        'views/pg_views.xml',
        'views/appartment_views.xml',
        'views/event_views.xml',
        'views/customer_invoice_views.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
    ],
}
