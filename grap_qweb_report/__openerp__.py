# -*- coding: utf-8 -*-
{
    'name': 'GRAP - Custom Qweb Reports',
    'version': '8.0.1.0.0',
    'category': 'GRAP - Custom',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'base_fiscal_company',
        'l10n_fr_siret',
        'purchase',
        'sale',
        'sale_recovery_moment',
        'sale_food',
        'product_print_category',
        'point_of_sale',
    ],
    'data': [
        'report/qweb_template_layout.xml',
        'report/qweb_template_account_invoice.xml',
        'report/qweb_template_picking_summary_wizard.xml',
        'report/qweb_template_purchase_order.xml',
        'report/qweb_template_purchase_order_quotation.xml',
        'report/qweb_template_sale_order.xml',
        'report/qweb_template_stock_picking.xml',
        'report/qweb_template_product_product.xml',
        'report/ir_actions_report_xml.xml',
        'views/action.xml',
        'views/templates.xml',
        'views/view_picking_summary_wizard.xml',
    ],
    'qweb': [
        'static/src/xml/grap_qweb_report.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
        'demo/product_print_category.xml',
    ],
}
