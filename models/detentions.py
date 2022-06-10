# -*- coding: utf-8 -*-
from datetime import datetime, date
from odoo import api, fields, models



class Detentions(models.Model):
    _name = "detentions.detention"
    _description = "Registros de Detenciones"
    _rec_name = "arrested_name"


    def _get_default_invoice(self):
        sequence_id = self.env['ir.sequence'].search(
            [('code', '=', 'sequence.detentions.folio')])
        if sequence_id:
            date_sequence = datetime.strftime(datetime.now(), '%y%m')
            number_next_actual = str(sequence_id.number_next_actual)
            return 'SVI/%s%s' % (date_sequence, number_next_actual)
        else:
            return datetime.strftime(datetime.now(), '%y%m%d%H%M%S')

    # BASIC FIELDS ADDDED
    invoice =fields.Char('No. De Folio', required=True, help="Número de Folio", readonly=True, default=_get_default_invoice)
    arrested_name = fields.Char("Nombre del Detenido", required=True)
    personal_phone = fields.Char(string='Teléfono Personal',required=True)
    arrested_address = fields.Char("Dirección del Detenido",required=True)
    tiene_lesiones = fields.Selection(string='Tiene Lesiones?',
                                      selection=[("no", "No"),("si", "Si")
                                                 ], required=True)
    responsable_id = fields.Many2one("hr.employee",string='Numero de empleado Responsable', required=True)
    responsable_nombre = fields.Char("Responsable",
                                     related="responsable_id.name", required=True)
    corporation_responsable = fields.Char("Corporacion del responsable" ,
                                     related = "responsable_id.company_id.name")

    status = fields.Selection(string='Estatus',
                                 selection=[("internamiento","Internamiento"),
                                            ("libertad","Libertad")
                                            ], required=True)
    entry_type = fields.Selection(string='Ingreso por:',
                                  selection=[("falta_administrativa","Falta Administrativa"),("delito","Delito")
                                             ])

    turno = fields.Selection(string= 'Turno',
                                  selection=[("vespertino", "Vespertino"),("diurno","Diurno")
                                        ], required=True)
    capturista_id = fields.Many2one("hr.employee",string='Capturista',required=True)
    capturista_nombre = fields.Char("capturista",
                                     related="capturista_id.name", required=True)
    coments = fields.Text("Comentarios")
    movements_ids = fields.One2many('detentions.movements','detention_id', string= 'Movimientos')
    documents_ids = fields.Many2many('ir.attachment', string='Documentos')

    @api.model
    def create(self, vals_list):
        vals_list["invoice"]=self.env['ir.sequence'].next_by_code('sequence.detentions.folio') or 'Unasigned'
        return super(Detentions,self).create(vals_list)
    # FIELDS WORKING INFORMATION ADDED


    # FEILDS ADDRESS ADDED


    # FIELDS OF MEDIA AFILIAICIÓN





