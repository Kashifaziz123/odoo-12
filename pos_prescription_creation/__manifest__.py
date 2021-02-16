{
    'name': 'Create Products From POS',
    'version': '13.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Create Products From POS Interface',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'images': ['static/description/banner.png'],
    'website': 'https://www.cybrosys.com',
    'depends': ['point_of_sale'],
    'data': [
             'views/pos_template.xml',
            ],
    'qweb': ['static/src/xml/pos.xml','static/src/xml/prescription_history.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
