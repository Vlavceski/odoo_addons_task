from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _create_packed_picking(self, operation_type, stock_move_data, owner=None,
                               location=None, location_dest_id=None, package_name=None,
                               create_lots=False, set_ready=False):
        location = location or operation_type.default_location_src_id
        location_dest_id = location_dest_id or operation_type.default_location_dest_id

        picking_vals = {
            'picking_type_id': operation_type.id,
            'location_id': location.id,
            'location_dest_id': location_dest_id.id,
            'partner_id': owner.id if owner else None,
        }

        picking = self.env['stock.picking'].create(picking_vals)

        for move_data in stock_move_data:
            product_id, qty_done, serial = move_data
            product = self.env['product.product'].browse(product_id)

            if not product:
                raise ValidationError(f"Product with ID {product_id} does not exist.")

            move_vals = {
                'picking_id': picking.id,
                'product_id': product.id,
                'product_uom_qty': qty_done,
                'product_uom': product.uom_id.id,
                'location_id': location.id,
                'location_dest_id': location_dest_id.id,
                'name': product.name,
            }

            move = self.env['stock.move'].create(move_vals)
            move.write({'quantity_done': qty_done})
            if create_lots and serial:
                self.env['stock.production.lot'].create({
                    'product_id': product_id,
                    'name': serial
                })

        if package_name:
            package = self.env['stock.quant.package'].create({'name': package_name})
            picking.move_line_ids.write({'result_package_id': package.id})

        if set_ready:
            picking.action_confirm()
            picking.action_assign()

        return picking
