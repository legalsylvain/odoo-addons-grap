# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# @author Julien WESTE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'GRAP - Change Views',
    'version': '8.0.7.0.0',
    'category': 'GRAP - Custom',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'account_invoice_supplierinfo_update',
        'account_statement_reconciliation',
        'stock_inventory_merge',
        'stock_inventory_valuation',
        'base_vat',
        'crm',
        'delivery',
        'mail',
        'email_template',
        'sale_food',
        'point_of_sale',
        'project',
        'product',
        'product_standard_margin',
        'product_standard_price_tax_included',
        'procurement',
        'purchase',
        'sale',
        'sale_margin',
        'sale_stock',
        'stock',
        'knowledge',
        'pos_multicompany',
        'pos_sector',
        'account_product_fiscal_classification',
        'sale_eshop',
        'product_to_scale_bizerba',
        'product_fiscal_company',
        'product_category_recursive_property',
        'l10n_fr',
        'sale_order_dates',
        'sale_recovery_moment',
        'pos_order_pricelist_change',
        'grap_cooperative',
        'web_dashboard_tile',
        'stock_picking_mass_action',
        'product_ean_duplicates',
        'simple_tax_account',
        'simple_tax_sale',
        'simple_tax_purchase',
        'purchase_discount',
        'intercompany_trade_base',
        'intercompany_trade_account',
        'recurring_consignment',
        'grap_change_access',
        'product_ean13_image',
        'barcodes_generator_product',
        'product_margin_classification',
        'product_sale_tax_price_included',
        'account_invoice_supplierinfo_update_standard_price',
        'account_invoice_triple_discount',
        'web_tree_dynamic_colored_field',
        'grap_qweb_report',
        'invoice_verified_state',
    ],
    'data': [
        'security/res_groups.yml',
        'views/view_account_bank_statement.xml',
        'views/view_account_bank_statement_line.xml',
        'views/view_account_invoice.xml',
        'views/view_account_invoice_line.xml',
        'views/view_account_journal.xml',
        'views/view_account_move.xml',
        'views/view_account_move_line.xml',
        'views/view_account_tax_template.xml',
        'views/view_account_voucher.xml',
        'views/view_ir_values.xml',
        'views/view_pos_category.xml',
        'views/view_pos_order.xml',
        'views/view_pos_order_line.xml',
        'views/view_pos_session.xml',
        'views/view_pos_session_opening.xml',
        'views/view_procurement_rule.xml',
        'views/view_product_category.xml',
        'views/view_product_margin_classification.xml',
        'views/view_product_pricelist_item.xml',
        'views/view_product_product.xml',
        'views/view_product_supplierinfo.xml',
        'views/view_project.xml',
        'views/view_purchase_order.xml',
        'views/view_res_company.xml',
        'views/view_res_partner.xml',
        'views/view_res_users.xml',
        'views/view_sale_order.xml',
        'views/view_stock_inventory.xml',
        'views/view_stock_inventory_line.xml',
        'views/view_stock_location.xml',
        'views/view_stock_move.xml',
        'views/view_stock_picking.xml',
        'views/view_stock_picking_type.xml',
        'views/view_stock_transfer_details.xml',
        'views/view_stock_warehouse.xml',
        'views/view_workflow_instance.xml',
        'views/view_workflow_workitem.xml',
        'views/view_wizard_update_invoice_supplierinfo.xml',
        'views/action.xml',
        'views/menu.xml',
        'views/grap_change_views.xml',
    ],
    'qweb': [
        'views/grap_change_views_qweb.xml',
    ],
    'demo': [
        'demo/res_groups.xml',
    ],
}
