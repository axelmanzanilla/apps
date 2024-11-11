{
    "name": "Main Menu",
    "version": "1.0.0",
    "summary": "Enhanced navigation module for Odoo Community Edition.",
    "description": """
        This module provides a centralized main menu for Odoo Community Edition, allowing users to quickly access core modules and enhance their workflow.
        It features widget functionality for displaying the current date and posting announcements, which can be managed by administrators.
    """,
    "author": "Axel Manzanilla",
    "maintainer": "Axel Manzanilla",
    "website": "https://axelmanzanilla.com",
    "license": "LGPL-3",
    "category": "Technical/Technical",
    "depends": [
        "mail",
    ],
    "data": [
        "views/res_config_setting_views.xml",
        "views/main_menu_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "main_menu/static/src/components/**/*",
        ],
    },
    "images": [
        "static/description/banner.png",
    ],
    "auto_install": True,
    "application": True,
    "installable": True,
}
