# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import _, api, fields, models



class Movements(models.Model):
    _name = "detentions.movements"
    _description = "Movimientos de PPL"

    fecha_hora = fields.Datetime('Fecha de Movimiento', required=True, help="fecha y hora de ingreso")
    documento_id = fields.Many2many('ir.attachment',
                                          string='Numero de documento')
    no_oficio = fields.Char(string='Numero de oficio')
    ordenante = fields.Char('Ordenante')
    dependencia_ordenante = fields.Char('Dependencia del ordenante')
    es_empleado_entregante = fields.Boolean(string='¿El entregante es empleado?')
    entregante_id = fields.Many2one('hr.employee', 'Entregante')
    entregante_nombre = fields.Char('Nombre de entregante', related = "entregante_id.name")
    es_empleado_receptor = fields.Boolean(string='¿El receptor es empleado?')
    receptor_id = fields.Many2one('hr.employee','Receptor')
    receptor_nombre = fields.Char('Nombre del receptor', related="receptor_id.name")
    entregante_dependencia = fields.Char('Dependencia del entregante', related="entregante_id.company_id.name")
    receptor_dependencia = fields.Char('Dependencia el Receptor', related="receptor_id.company_id.name")
    entregante = fields.Char('Entregante')
    receptor = fields.Char('Receptor')
    unidad = fields.Char('Unidad')
    tipo_movimineto_id = fields.Many2one('detentions.type.movements',"Tipo de movimiento")
    detention_id = fields.Many2one('detentions.detention', 'Detentions')
    notas = fields.Text('Notas')
