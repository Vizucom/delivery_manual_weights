# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2017- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Manual Weight Fields for Stock Picking',
    'category': 'Stock',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['delivery'],
    'description': """
Manual Weight Fields for Stock Picking
======================================
* Adds the option to input weight and net weight manually to Stock Picking instead of having the delivery module calculate them based on Stock Moves.
* Note: these fields do not currently affect the delivery cost calculation in any way, they are intended only for adding weight info to Dispatch Note prints in cases when products do not have weight info
""",
    'data': [
        'views/stock_picking.xml',
    ],
}
