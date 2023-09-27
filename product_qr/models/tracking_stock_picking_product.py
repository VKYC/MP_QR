from odoo import _, api, fields, models


class TransferStockPickingProduct(models.Model):
    _name = 'transfer.stock.picking.product'
    _description = 'Transfer Stock Picking Product'

    name = fields.Char(string='Name', required=True, default=lambda self: _('New'))
    product_id = fields.Integer(string='Product', required=True)
    model = fields.Char(string='Model', required=True)
    page = fields.Integer(string='Page', required=True)
    row = fields.Integer(string='Row', required=True)
    column = fields.Integer(string='Column', required=True)
    picking_id = fields.Many2one('stock.picking', string='Picking', required=True)

    _sql_constraints = [
        ("page_row_column_picking_product_model_unique", "unique(page, row, column, picking_id, product_id, model)", "Page, Row, Column and Picking Product must be unique!"),
    ]

    def get_code_for_qr(self, page, row, column, picking_id, product_id, model):
        record = self.search([('page', '=', page), ('row', '=', row), ('column', '=', column), ('picking_id', '=', picking_id), ('product_id', '=', product_id), ('model', '=', model)])
        if not record:
            record = self.create({'page': page, 'row': row, 'column': column, 'picking_id': picking_id, 'product_id': product_id, 'model': model})
        return record.name

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('transfer.stock.picking.product') or _('New')
        result = super(TransferStockPickingProduct, self).create(vals)
        return result
