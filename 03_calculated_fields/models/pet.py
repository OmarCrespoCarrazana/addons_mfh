from odoo import api, fields, models


class Pet(models.Model):
    _inherit = 'ej.pet'
    code = fields.Char(string='Code', default='New', readonly=1)
    pet_sound = fields.Char('Pet sounds', compute='_compute_sound')
    mydb = fields.Char(default=lambda self: self.env.cr.dbname, string='DB')

    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ej.pet') or "New"
        pet = super(Pet, self).create(vals)
        return pet

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
