
{
    'name': 'Pos Optical Erp',
    'version': '1.0.0',
    'category': 'hidden',
    'sequence':2,
    'summary': 'Pos Optical Erp',
    'description': "",
    'depends': ['stock_account','point_of_sale','barcodes', 'web_editor','digest','optical_erp'],
    'data': [
        'views/point_of_sale_template.xml',
    ],

    'installable': True,
    'auto_install': False,
    'qweb': ['static/src/xml/prescription_history.xml'],


}
