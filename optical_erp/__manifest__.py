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
    "website": "alhaditech.com",
    "license": "OPL-1",
    'images': ['static/description/background.png'],
    "depends": ['base','doctor', 'patient', 'sale', ],
    'price': 80, 'currency': 'EUR',
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "view/test_type.xml",
        "view/prescription.xml",
        'view/patient_inherit.xml',
        'view/doctor_inherit.xml',
        "view/view.xml",
    ],
    "installable": True,
    'application': True,
}
