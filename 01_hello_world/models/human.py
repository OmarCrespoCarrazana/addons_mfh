from odoo import api, fields, models


class Human(models.Model):
    _name = 'human'
    name = fields.Char(string='Name', required=True)
    id_number = fields.Char(string='Id Number', required=True)
    # age = campo auto calculable
    gender = fields.Char(string="Gender", compute='_compute_the_gender_from_id_number')
    blood_type = fields.Selection([('A+', 'A+'),
                                   ('A-', 'A-'),
                                   ('B+', 'B+'),
                                   ('B-', 'B-'),
                                   ('AB+', 'AB+'),
                                   ('AB-', 'AB-'),
                                   ('O+', 'O+'),
                                   ('O-', 'O-')], string='Blood Group', default="A+")

    @api.depends('id_number')
    def _compute_the_gender_from_id_number(self):
        for record in self:
            penultimate_number = int(record.id_number[10])
            if penultimate_number % 2 == 0:
                record.gender = 'Male'
            else:
                record.gender = 'Female'



