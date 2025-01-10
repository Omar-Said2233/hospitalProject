# -*- coding: utf-8 -*-
{
    'name': "my school",

    'summary': """
        test app in odoo""",

    'description': """
        for my school
    """,

    'author': "Omar sayed",


    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail','board'],

    # always loaded
    'data': [
        # 'security/security_views.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/my_contact_view.xml',
        # 'views/dashbord.xml',
        'reports/my_report.xml'
    ],
    # only loaded in demonstration mode
    'application': True,
}
