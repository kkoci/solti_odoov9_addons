# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  BMyA SA  (http://blancomartin.cl)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": """Chile - Web Services de Documentos Tributarios Electrónicos\
    """,
    'version': '8.0.0.0.1',
    'category': 'Solti',
    'sequence': 12,
    'author':  'Kristian Koci - tomando como base el modulo de bmya',
    'website': 'http://blancomartin.cl',
    'license': 'AGPL-3',
    'summary': '',
    'description': """
Chile: API and GUI to access Electronic Invoicing webservices.
===============================================================
""",
    'depends': [
        'webservices_solti',
        'ubicaciones_chile_solti',
        'invoice_solti',
        'manejo_caf_solti',
        ],
    'external_dependencies': {
        'python': [
            'xmltodict',
            'dicttoxml',
            'elaphe',
            'M2Crypto',
            'base64',
            'hashlib',
            'cchardet'
        ]
    },
    'data': [
        'views/invoice_view.xml',
        'views/partner_view.xml',
        'views/company_view.xml',
        'views/payment_t_view.xml',
        'views/sii_regional_offices_view.xml',
        #'data/sii.regional.offices.csv',
        'security/ir.model.access.csv',
        'views/layouts.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
