{
    "name": "POS User Own Session",
    "version": "12.0.0.0.1",
    "category": "",
    "author": "Object Synergy",
    "website": "https://www.objectsynergy.com",
    "license": "OPL-1",
    "depends": [
        'base','point_of_sale',
    ],
    'category': 'Point Of Sale',
    'price': 10, 'currency': 'EUR',
    "data": [
        "security/ir.model.access.csv",
        "view/rules.xml",
        "view/view.xml",
    ],
    "installable": True,
    'application': True,
}
