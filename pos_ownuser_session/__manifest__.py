{
    "name": "POS User Own Session",
    "version": "12.0.0.0.1",
    "category": "",
     'summary': "POS userwise session",
    'description': """
    odoo Pos user can access own sessions.
    """,
    "author": "Kashif Aziz",
    "website": "https://www.objectsynergy.com",
    "license": "OPL-1",
   'images': ['static/description/visible_session (1).png'],
    "depends": [
        'base','point_of_sale',
    ],
'price': 10, 'currency': 'EUR',  
,
    'category': 'Point Of Sale',
    "data": [
        "security/ir.model.access.csv",
        "view/rules.xml",
        "view/view.xml",
    ],
    "installable": True,
    'application': True,
}
