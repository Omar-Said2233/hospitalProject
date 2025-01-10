{
    'name': "my hospital",
    'summary': """
        test app in odoo
    """,
    'description': """
        for my hospital
    """,
    'author': "Omar sayed",
    'category': 'Uncategorized',
    'version': '0.1',

    # أي موديل آخر يعتمد عليه هذا الموديل لكي يعمل بشكل صحيح
    'depends': ['base', 'mail'],

    # ملفات البيانات الخاصة بالموديل
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/views.xml',
        'views/doctor.xml',
        'views/appointments.xml',
        'views/menus.xml',
    ],

    # لتحديد إذا كان التطبيق تطبيقًا قابلاً للاستخدام
    'application': True,
}



