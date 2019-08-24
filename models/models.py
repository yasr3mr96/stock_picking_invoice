# -*- coding: utf-8 -*-

from odoo import models, fields, api

class stock_picking_invoice(models.Model):
    _inherit = 'stock.picking'
    account_id = fields.Many2one('account.account', string='Account',
                                  states={'draft': [('readonly', False)]},
                                 domain=[('deprecated', '=', False)], help="The partner account used for this invoice.",required=True)
    journal_id = fields.Many2one('account.journal', string='Journal',required=True)

    def generate_inv(self):
        lines = []
        stock = self.env['stock.picking'].browse(self.env.context['active_id'])
        for i in stock.move_line_ids_without_package:
            lines.append((0, 0, {'account_id': i.product_id.categ_id.property_account_income_categ_id.id,
                                 'product_id': i.product_id.id, 'name': i.product_id.name, 'quantity': i.qty_done,
                                 'discount': 0, 'price_unit': i.product_id.standard_price}))

        self.env['account.invoice'].create({'invoice_line_ids': lines, 'journal_id': stock.journal_id.id, 'partner_id':stock.partner_id.id, 'account_id': stock.account_id.id})

        return  {
                'type': 'ir.actions.act_window',
                'res_model': 'account.invoice',
                'view_mode':'tree'
                            }




