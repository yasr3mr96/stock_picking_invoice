# -*- coding: utf-8 -*-
{
    'name': "stock_picking_invoice",

    'summary': """
       stock_picking_invoice""",

    'description': """
       stock_picking_invoice
    """,

    'author': "Yasser Omar",
    'website': "http://www.facebook.com/yasr3mr96",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'stock',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
