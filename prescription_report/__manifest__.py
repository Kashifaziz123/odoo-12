{
    "name": "Prescription Report",
    "version": "13.0.0.0.1",
    "category": "Optical",
    "version": "13.0.0.0.1",
    'summary': "Solution for Optical(EYE) shops and clinics",
    'description': """
    odoo Solution for Optical(EYE) shops and clinics.
    """,
    "author": "Alhaditech",
    "website": "alhaditech.com",
    "license": "OPL-1",
    'images': ['static/description/background.png'],
    "depends": [
        'base','sale','optical_erp'
    ],
    'price': 10, 'currency': 'EUR',
    "data": [
        "report/reports.xml",
        "report/prescription_report.xml",

    ],
    "installable": True,
    'application': True,
}
