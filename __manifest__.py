# -*- coding: utf-8 -*-
{
    'name': "routes",

    'summary': """
        This module has useful tools to manage and see all the routes' data.""",

    'description': """
        The tools provides different graphs to see in a clearer way data such as
        how many packages have been sent, the distance a certain worker has 
        travelled, the time a worker has been on the road...
    """,

    'author': "Jon Calvo, Unai Pérez, Daira Eguzkiza",
    'website': "https://es.linkedin.com/in/eusko-code-866723198",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}