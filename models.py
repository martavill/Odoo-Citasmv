# -*- coding: utf-8 -*-

from odoo import models, fields, api

class citasmv(models.Model):
 _name = 'citasmv.citasmv'
  name = fields.char(string="Autor:", size=100, required=True),
  fecha = fields.date(string="Fecha de visualizaciòn:", required=True),
  description = fields.text(string="Descripciòn de la cita:", size=256, required=True),
  orden = fields.integer(string="Orden de visualizaciòn:", required=True)

  