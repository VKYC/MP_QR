{
    'name': 'Product QR',
    'version': '1.0',
    'description': '',
    'summary': '',
    'author': '',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'product', 'base_accounting_kit', 'qr_generator', 'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/product_views.xml',
        'views/product_label_layout_views.xml',
        'report/product_product_templates.xml',
    ],
    'demo': [

    ],
    'auto_install': False,
    'application': False,
    'assets': {

    }
}
