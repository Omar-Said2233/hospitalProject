{
    'name': "app one",
    'version': '1.0',
    'author': "omar sayed",
    'category': '',
    'depends': ['base','mail','contacts','web'
                # 'sale_management',
                # 'account_accountant'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_minu.xml',
        'views/property_views.xml',
        'views/owner_views.xml',
        'views/tag_views.xml',
        'views/building_views.xml',
        'reports/property_report.xml',
    ],
    'assets': {
        'wed.assets_backend': ['app_one/static/src/css/property.css',],
    },
    'application': True,
    'installable': True,
}
