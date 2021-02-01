{
    "name": "Optical ERP",
    "version": "13.0.0.0.1",
    "category": "Optical",
    "version": "13.0.0.0.1",
    'summary': "Solution for Optical(EYE) shops and clinics",
    'description': """
    odoo Solution for Optical(EYE) shops and clinics.
    """,
    "author": "Alhaditech",
    "website": "www.alhaditech.com",
    "license": "OPL-1",
    'images': ['static/description/background.png'],
    "depends": [
        'base','sale','doctor'
    ],
    'price': 120, 'currency': 'EUR',
    "data": [
        'security/groups.xml',
        "security/ir.model.access.csv",
        "data/data.xml",
        "data/sequence.xml",
        "report/reports.xml",
        "report/prescription_report.xml",
        "views/prescription.xml",
        "views/res_config_settings_views.xml",
        "views/partner.xml",
        "views/test_type.xml",
    ],
    "installable": True,
    'application': True,
}
