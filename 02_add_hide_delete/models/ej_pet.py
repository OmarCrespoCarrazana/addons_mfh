from odoo import api, models, fields


class EjPet(models.Model):
    _inherit = 'ej.pet'
    owners_age = fields.Integer('Owner age')
    weight = fields.Float('Weight in pounds')
