{
    "name": "Optical ERP",
    "version": "12.0.0.0.1",
    "category": "Optical",
    "version": "12.0.0.0.1",
    'summary': "Solution for Optical(EYE) shops and clinics",
    'description': """
    odoo Solution for Optical(EYE) shops and clinics.
    """,
    "author": "Alhaditech",
    "website": "https://alhaditech.com",
    "license": "OPL-1",
    'images': ['static/description/background.png'],
    "depends": [
        'base','sale','dr',
    ],
'price': 50, 'currency': 'EUR',
    "data": [
        "security/ir.model.access.csv",
        "view/view.xml",
    ],
    "installable": True,
    'application': True,
}
