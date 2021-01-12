{
    "name": "doctor",
    "version": "12.0.0.0.1",
    "category": "setting",
    "author": "Alhaditech",
    'support': 'https://alhaditech.com',
    "license": "OPL-1",
    'images': ['static/description/dr.jpg'],
    "depends": [
        'base',
    ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "security/security.xml",
        "view/doctor_wizard.xml",
        "view/doctor.xml",
    ],
    "installable": True,
}
