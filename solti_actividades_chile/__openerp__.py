# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
    'active': False,
    'author': u'Kristian Koci - Inspirado en el modulo de bmya',
    'category': 'Contabilidad chilena',
    'demo_xml': [],
    'depends': ['account'],
    'description': u'''
        Actividades Económicas chilenas.
        Fuente: http://www.sii.cl/catastro/codigos.htm
    ''',
    'init_xml': [],
    'installable': True,
    'license': 'AGPL-3',
    'name': u'Actividades Económicas',
    'test': [],
    'data': [
        # 'security/l10n_cl_partner_activities.xml',
        'data/partner.activities.csv',
        'views/sii_menuitem.xml',
        'views/partner_activities.xml',
        'views/invoice_turn.xml',
        'security/ir.model.access.csv',
    ],
    'website': 'https://kkoci.github.io'
}
