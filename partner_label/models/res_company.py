# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    partner_labels_width = fields.Float(
        'Width (mm)', default=60, help='Width in millimeters', required=True,
    )
    partner_labels_height = fields.Float(
        'Height (mm)', default=42.3, help='Height in millimeters', required=True,
    )
    partner_labels_padding = fields.Float(
        'Padding (mm)', default=5, help='Padding in millimeters', required=True,
    )
    partner_labels_margin_top = fields.Float(
        string="Margin Top (mm)",
        default=1,
        help="Margin top in millimeters",
        required=True,
    )
    partner_labels_margin_bottom = fields.Float(
        string="Margin Bottom (mm)",
        default=1,
        help="Margin bottom in millimeters",
        required=True,
    )
    partner_labels_margin_left = fields.Float(
        string="Margin Left (mm)",
        default=1,
        help="Margin left in millimeters",
        required=True,
    )
    partner_labels_margin_right = fields.Float(
        string="Margin Right (mm)",
        default=1,
        help="Margin right in millimeters",
        required=True,
    )
