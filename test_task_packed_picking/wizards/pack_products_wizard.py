from odoo import models, fields, api


class PackProductsWizard(models.TransientModel):
    _name = 'pack.products.wizard'
    _description = 'Pack Products Wizard'

    picking_type_id = fields.Many2one('stock.picking.type', string='Operation Type', required=True)
    owner_id = fields.Many2one('res.partner', string='Owner')
    location_id = fields.Many2one('stock.location', string='Source Location')
    location_dest_id = fields.Many2one('stock.location', string='Destination Location')
    package_name = fields.Char(string='Package Name')
    set_ready = fields.Boolean(string='Set Ready')
    create_lots = fields.Boolean(string='Create Lots')
    stock_move_data = fields.One2many('pack.products.wizard.line', 'wizard_id', string='Stock Move Data')

    def create_packed_picking(self):
        stock_move_data = [(line.product_id.id, line.qty_done, line.serial) for line in self.stock_move_data]
        self.env['stock.picking']._create_packed_picking(
            self.picking_type_id,
            stock_move_data,
            owner=self.owner_id,
            location=self.location_id,
            location_dest_id=self.location_dest_id,
            package_name=self.package_name,
            create_lots=self.create_lots,
            set_ready=self.set_ready
        )
