
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'
    
    # data = fields.Char('Data', default='')
    qr_code = fields.Binary('QR Code', attachment=True, store=True, compute='compute_qr_code')

    @api.depends('product_tmpl_ids', 'product_ids')
    def compute_qr_code(self):
       
        for wizard in self:
            if wizard.product_tmpl_ids:
                products = wizard.product_tmpl_ids
            elif wizard.product_ids:
                products = wizard.product_ids
            if len(products) == 1:
                wizard.qr_code = self.env['qr.generator'].get_qr_code(products.name)
            else:
                wizard.qr_code = False