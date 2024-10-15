from odoo.tests import TransactionCase


class TestPackedPicking(TransactionCase):

    def setUp(self):
        super(TestPackedPicking, self).setUp()

        self.location_src = self.env['stock.location'].create({
            'name': 'Source Location'
        })
        self.location_dest = self.env['stock.location'].create({
            'name': 'Destination Location'
        })

        self.operation_type = self.env['stock.picking.type'].create({
            'name': 'Test Operation Type',
            'sequence_code': 'TEST_OP',
            'code': 'outgoing',
            'default_location_src_id': self.location_src.id,
            'default_location_dest_id': self.location_dest.id,
            'use_create_lots': True,
            'use_existing_lots': True,
            'reservation_method': 'at_confirm',
            'create_backorder': 'ask'
        })
        self.product = self.env['product.product'].create({
            'name': 'TEST Product 1',
            'type': 'product'
        })

    def test_create_packed_picking(self):
        stock_move_data = [(self.product.id, 16.0, None)]

        picking = self.env['stock.picking']._create_packed_picking(
            self.operation_type, stock_move_data
        )

        self.assertTrue(picking, "Picking was not created")
        self.assertEqual(picking.state, 'draft', "Picking state is not 'assigned'")
        self.assertEqual(picking.picking_type_id, self.operation_type, "Picking type mismatch")

        self.assertEqual(picking.location_id, self.location_src, "Source location mismatch")
        self.assertEqual(picking.location_dest_id, self.location_dest, "Destination location mismatch")
