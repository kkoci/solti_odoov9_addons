# -*- coding: utf-8 -*-
{
    'author': u'Kristian Koci - tomando inspiracion del modulo CAF de bmya',
    'category': 'Solti - Archivos CAF',
    'depends': ['invoice_solti'],
    "external_dependencies": {
        'python': [
            'xmltodict',
            'base64'
        ]
    },
    'description': u'''\n\nDTE CAF File Data Model\n\n''',
    'installable': True,
    'license': 'AGPL-3',
    'name': 'Contenedor de archivos CAF',
    'test': [],
    'data': [
        'views/dte_caf.xml',
        'security/ir.model.access.csv',
    ],
    'update_xml': [],
    'version': '0',
    'website': 'https://kkoci.github.io',
    'auto-install': False,
    'active': False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
