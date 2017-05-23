-*- coding: utf-8 -*-
{
    'name': "Gestor de Citas para la empresa TECNODIGITAL",

    'summary': """
        Gestor de Citas para la empresa TECNODIGITAL
        Tarea 04 SGE """,

    'description': """
        Este mòdulo gestiona las citas en la empresa 
        TECNODIGITAL. 
        Va a permitir añadir el autor de la cita, la cita 
        y la fecha de visualizaciòn. 
        Ha sido creado por Marta Villalobos 
        como Tarea 04 de SGE. 
    """,

    'author': "TECNODIGITAL",
    'website': "http://www.tecnodigital.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/citasmv.xml',
        'views/templates.xml',
    ],
}