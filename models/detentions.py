# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import api, fields, models



class Detentions(models.Model):
    _name = "detentions.detention"
    _description = "Registros de Detenciones"

    # BASIC FIELDS ADDDED
    invoice = fields.Char('No. De Folio', required=True, help="Número de Folio")
    arrested_name = fields.Char("Nombre del Detenido", required=True)
    personal_phone = fields.Char(string='Teléfono Personal',required=True)
    arrested_address = fields.Char("Dirección del Detenido",required=True)
    tiene_lesiones = fields.Selection(string='Tiene Lesiones?',
                                      selection=[("no", "No"),
                                                 ("si", "Si")
                                                 ])
    responsable_id = fields.Many2one("hr.employee",string='Numero de empleado Responsable', required=True)
    responsable_nombre = fields.Char("Responsable",
                                     related="responsable_id.name", required=True)
    corporation_responsable = fields.Char("Corporacion del responsable" ,
                                     related = "responsable_id.company_id.name")

    status = fields.Selection(string='Estatus',
                                 selection=[("internamiento","Internamiento"),
                                            ("libertad","Libertad")
                                            ])
    entry_type = fields.Selection(string='Ingreso por :',selection=[("falta_administrativa","Falta Administrativa"),("delito","Delito")])

    turno = fields.Selection(string= 'Turno',
                             selection =[("vespertino", "Vespertino"),("diurno","Diurno")
                                        ], required=True)
    capturista_id = fields.Many2one("hr.employee",string='Capturista',required=True)
    capturista_nombre = fields.Char("capturista",
                                     related="capturista_id.name", required=True)
    coments = fields.Text("Comentarios")
    movements_ids = fields.Many2many('detentions.movements', string= 'Movimientos')
    documents_ids = fields.Many2many('ir.attachment', string='Documentos')


    # FIELDS WORKING INFORMATION ADDED


    # FEILDS ADDRESS ADDED


    # FIELDS OF MEDIA AFILIAICIÓN





