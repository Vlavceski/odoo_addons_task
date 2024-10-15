# Task description
Part 1
Create the following function in the stock.picking module
def _create_packed_picking(self,operation_type,stock_move_data,owner=None,
location=None,location_dest_id=None,package_name=None,create_lots=False,
set_ready=False,):
"""Create a picking and put its product into a package.
This is equal to the following sequence:
- Create a new picking
- Assign an owner
- Add products and set qty_done
- Mark as "Todo"
- Put in pack
Args:
operation_type (stock.picking.type): Operation type
stock_move_data (List of tuples): [(product_id, qty_done, serial)]
- (Integer) product_id: id of the product
- (float) qty_done: quantity done
- (Char, optional) serial: serial number to assign.
Default lot names will be used if is None or == False Used only if
'create_lots==True'
owner (res.partner, optional): Owner of the product
location (stock.location, optional): Source location if differs from the
operation type one
location_dest (stock.location, optional): Destination location if differs
from the operation type one
package_name (Char, optional): Name to be assigned to the package. Default
name will be used if not provided.
set_ready (bool, optional): Try to set picking to the "Ready" state.
Returns:
stock.picking: Created picking
"""
return picking
Part 2
- Add a wizard that allows the user to call the function and perform all the actions that it
allows to do.
- Create a new menu in the “Inventory” app: “Pack Products” and add the wizard to that
menu.
