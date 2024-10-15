from odoo import models, fields, api


class PackProductsWizardLine(models.TransientModel):
    _name = 'pack.products.wizard.line'
    _description = 'Pack Products Wizard Line'

    wizard_id = fields.Many2one('pack.products.wizard', string='Wizard')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    qty_done = fields.Float(string='Quantity Done', required=True)
    serial = fields.Char(string='Serial Number')
