# -*- coding: utf-8 -*-
{
    'name': "Binary Attachment URL",
    'summary': """
        Get URL of binary file as attachement store in file""",

    'description': """
        Long description of module's purpose
    """,
    'author': "Alhaditech",
    'website': "http://www.alhaditech.com",
    # for the full list
    'category': 'Attachement',
    'price': 60, 'currency': 'EUR',
    'version': '12.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
