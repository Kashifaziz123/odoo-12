{
    'name': 'Optical POS',
    'version': '13.0.1.0.0',
    'category': 'hidden',
    'summary': 'Optical Point of sale',
    'author': 'AlhadiTech Developed by Zain Irfan',
    'company': 'AlhadiTech',
    'images': ['static/description/banner.png'],
    'website': '',
    'depends': ['point_of_sale', 'optical_erp'],
    'data': [
             'views/pos_template.xml',
             'views/pos_order_view.xml',
             'views/product_attribute_view.xml',
             'data/optical_product_variants.xml',
            ],
    'qweb': ['static/src/xml/pos.xml', 'static/src/xml/prescription_history.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
