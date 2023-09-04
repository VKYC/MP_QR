from odoo import _, api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Product Template'

    @api.model
    def create(self, vals):
        vals["default_code"] = self.env["ir.sequence"].next_by_code(
            "seq.product.template.default_code"
        )
        return super(ProductTemplate, self).create(vals)
