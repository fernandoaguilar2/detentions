# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import  fields, models



class Detentions(models.Model):
    _name = "detentions.detentions"
    _description = "Registros de Detenciones"

    # BASIC FIELDS ADDDED
    invoice = fields.Char('No. De Folio', required=True, help="Número de Folio")
    arrested_name = fields.Char("Nombre del Detenido")
    personal_phone = fields.Char(string='Teléfono Personal')
    arrested_address = fields.Char("Dirección del Detenido")
    tiene_lesiones = fields.Selection(string='Tiene Lesiones?',
                                      selection=[("no", "No"),
                                                 ("si", "Si")
                                                 ])
    responsable_id = fields.Many2one("hr.employee",string='Numero de empleado Responsable')
    responsable_nombre = fields.Char("Responsable",
                                     related="responsable_id.name")
    corporation_responsable = fields.Char("Corporacion del responsable" ,
                                     related = "responsable_id.company_id")

    status = fields.Selection(string='Estatus',
                                 selection=[("internamiento","Internamiento"),
                                            ("libertad","Libertad")
                                            ])
    entry_type = fields.Selection(string='Ingreso por :',
                                    selection=[("falta_administrativa","Falta Administrativa"),
                                           ("delito","Delito")
                                            ])



    turno = fields.Selection(string= 'Turno',
                             selection =[("vespertino", "Vespertino"),("diurno","Diurno")
                                        ])
    capturista_id = fields.Many2one("hr.employee",string='Capturista')
    capturista_nombre = fields.Char("capturista",
                                     related="capturista_id.name")
    coments = fields.Text("Comentarios")
    movements_ids = fields.Many2many('detentions.movements', string= 'Movimientos')
    documents_ids = fields.Many2many('ir.attachment', string='Documentos')


    # FIELDS WORKING INFORMATION ADDED


    # FEILDS ADDRESS ADDED


    # FIELDS OF MEDIA AFILIAICIÓN





