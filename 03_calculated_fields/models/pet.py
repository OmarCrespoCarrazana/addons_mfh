from odoo import api, fields, models


class Pet(models.Model):
    _inherit = 'ej.pet'
    pet_sound = fields.Char('Pet sounds', compute='_compute_sound')
    mydb = fields.Char(default=lambda self: self.env.cr.dbname, string='DB')

    @api.onchange('species')
    def _compute_sound(self):
        for record in self:
            if record.species == 'dog':
                record.pet_sound = 'Bark'
            elif record.species == 'cat':
                record.pet_sound = 'Meow'
            elif record.species == 'bird':
                record.pet_sound = 'Chirp'
            else:
                record.pet_sound = "How should I know!"
