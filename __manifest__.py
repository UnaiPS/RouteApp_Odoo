# -*- coding: utf-8 -*-
{
    'name': "Routes",

    'summary': """
        Route's, directions' and delivery users' management.
        """,

    'description': """
        This module handles the user the options to enter routes with its 
        respective deliveryman, admin who created it, origin and destinations. 
        It also gives you the possibility 
        to add delivery users and to see stats based on the routes travelled.
    """,

    'author': "EuskoCode",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/security.xml',
       'security/ir.model.access.csv',
        'views/route_view.xml',
        'views/routeuser_view.xml',
#       'views/route_stats_view.xml',
#        'report/route_stats_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}