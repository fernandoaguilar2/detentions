from odoo import _, api, fields, models



class Type_movements(models.Model):
    _name = "detentions.type.movements"
    _description = "Tipo de Movimientos de PPL"
    _rec_name = 'nombre_tipo_movimiento'

    nombre_tipo_movimiento = fields.Char("Nombre del tipo de movimiento")
    descripcion_tipo_movimiento = fields.Char("Descripción del tipo de movimiento")