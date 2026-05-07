# -*- coding: utf-8 -*-
{
    'name': 'POS Cashdrawer Action Menu',
    'version': '19.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Move the POS cashdrawer action to the action menu',
    'description': """
Adds the cashdrawer opening action to the Point of Sale action menu.

The module reuses the native Odoo hardware proxy cashdrawer behavior, so it
works with any supported POS cashdrawer setup, including Epson ePOS and IoT.
    """,
    'author': 'Cositt Technology',
    'website': 'https://cositt.com',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'cs_pos_cashdrawer_menu/static/src/xml/cashdrawer_menu.xml',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

