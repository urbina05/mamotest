# -*- coding: utf-8 -*-
{
    'name': "Persiscal Theme",

    'summary': """
        Persiscal Consulting Odoo Theme""",

    'description': """
        Persiscal Consulting Odoo Theme
    """,

    'author': "Persiscal Consulting LLC",
    'website': "https://www.persiscalconsulting.com",

    'category': 'Theme/Backend',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['web_enterprise'],

    # always loaded
    'data': [
        'views/templates.xml',
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'images': ['static/description/icon.png'],
}