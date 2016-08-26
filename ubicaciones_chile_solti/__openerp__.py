# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    Copyright (C) 2013 Cubic ERP - Teradata SAC.
#    Copyright (C) 2016 Blanco Martín & Asociados - Odoo Chile Community
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
    "name": "Regiones chilenas para el flujo de Solti",
    "version": "0",
    "description": """
Chilean Regions, Cities and Counties .
Lista de regiones, ciudades y comunas de Chile
    """,
    "author": "Kristian Koci - tomando inspiracion del modulo CAF de bmya",
    "website": "https://kkoci.github.io",
    "category": "Regiones chilenas para SOlti",
    "depends": [
        "base_state_ubication",
    ],
    "data":[
        "data/l10n_cl_counties_data.xml",
        "views/res_partner_view.xml",
        "views/res_state_view.xml"
        ],
    "active": False,
    "installable": True,
}
