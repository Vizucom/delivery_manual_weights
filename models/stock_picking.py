# -*- coding: utf-8 -*-
from openerp import models, fields
import openerp.addons.decimal_precision as dp


class StockPicking(models.Model):

    _inherit = 'stock.picking'

    use_manual_weights = fields.Boolean('Manual weights', help='''Type in weights manually instead of having them calculated based on products.''')
    weight_manual = fields.Float('Weight (manual)', digits_compute=dp.get_precision('Stock Weight'), help='''Manual gross weight''')
    weight_net_manual = fields.Float('Net Weight (manual)', digits_compute=dp.get_precision('Stock Weight'), help='''Manual net weight''')
