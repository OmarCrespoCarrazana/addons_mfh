from odoo import api, models, fields


class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char('Name', required=True)
    age = fields.Float('Age in Years', required=True)
    color = fields.Char('Color')
    species = fields.Selection(selection=[('dog', "Dog"),
                                          ('cat', "Cat"),
                                          ('bird', "Bird"),
                                          ('other', "Other")], required=True, default='dog')
    size = fields.Selection([('small', 'Small'),
                             ('medium', 'Medium'),
                             ('big', 'Big')], 'Size', required=True)

    # Fields to be used in next exersice

    my_age = fields.Integer('Should be the Owners Age', required=True)
    remove_me = fields.Boolean('Will be removed', default=True)
