# -*- coding: utf-8 -*-
##############################################################################
#
#    @package to_pos_shared_floor TO POS Shared Floor for Odoo 9.0
#    @copyright Copyright (C) 2015 T.V.T Marine Automation (aka TVTMA). All rights reserved.#
#    @license http://www.gnu.org/licenses GNU Affero General Public License version 3 or later; see LICENSE.txt
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

import logging
from openerp import api, fields, models, _
from openerp.exceptions import UserError, ValidationError
from openerp.tools.safe_eval import safe_eval as eval

class solti(models.Model):

    """Inherits account.invoice.refund and adds journal_id field"""
    #_name = "solti.refund"
    _inherit = "account.invoice.refund"

    _columns = {
       'journal_id': fields.Many2one('account.journal', 'Refund Journal', help='You can select here the journal to use for the credit note that will be created. If you leave that field empty, it will use the same journal as the current invoice.'),
    }