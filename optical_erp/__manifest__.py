{
    "name": "Optical ERP",
    "version": "13.0.0.0.1",
    "category": "Optical",
    "version": "13.0.0.0.1",
    'summary': "Solution for Optical(EYE) shops and clinics",
    'description': """
    odoo Solution for Optical(EYE) shops and clinics.
    """,
    "author": "Kashif Aziz",
    "website": "alhaditech",
    "license": "OPL-1",
    'images': ['static/description/background.png'],
    "depends": [
        'base','sale','dr',
    ],
'price': 26, 'currency': 'EUR',
    "data": [
        "security/ir.model.access.csv",
        "view/view.xml",
    ],
    "installable": True,
    'application': True,
}
