# -*- coding: utf-8 -*-
{   'active': False,
    'author': u'Kristian Koci',
    'website': 'https://kkoci.github.io',
    'category': 'Solti',
    'depends': [
        'invoice_solti'
        ],
    'description': u'''
\n\nMódulo que simplifica la terminología para usuarios basicos.
Se recomienda instalar sólo en caso de usuarios con poco nivel de conocimiento
contable, y para uso en mesón.
''',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Solti - temrinología usuarios sii',
    'data': [
        'data/responsability.xml',
        'data/partner.xml',
        'data/sii.document_letter.csv',
        'data/sii.document_class.csv',
    ],
    'version': '0.1',
}
