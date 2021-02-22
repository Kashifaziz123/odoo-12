{
    'name': 'Optical POS',
    'version': '13.0.1.0.0',
    'category': 'hidden',
    'summary': 'Create Products From POS Interface',
    'author': 'AHT',
    'company': 'Cybrosys Techno Solutions',
    'images': ['static/description/banner.png'],
    'website': 'https://www.cybrosys.com',
    'depends': ['point_of_sale'],
    'data': [
             'views/pos_template.xml',
             'views/pos_order_view.xml'
            ],
    'qweb': ['static/src/xml/pos.xml','static/src/xml/prescription_history.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
