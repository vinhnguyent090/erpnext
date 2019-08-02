# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals

no_cache = 1
no_sitemap = 1

import frappe
from erpnext.shopping_cart.cart import get_cart_quotation
# from erpnext.shopping_cart.cart import get_party
from bellamar_website.utils.cart_custom import get_cart_quotation


def get_context(context):
    context.update(get_cart_quotation())
    login_user=get_party()
    login_name=login_user.name
    context.login_name=login_name
    customer_group=frappe.db.sql("""select customer_group from `tabCustomer` where name='{0}' """.format(login_name))
    customer_group_list=[]
    for cs in customer_group:
        for cs_t in cs:
            customer_group_list.append(cs_t)
    cusg=''.join(customer_group_list)
    context.cusg=cusg
    parent=frappe.db.sql("""select parent from `tabCoupon Customer group` where customer_group='{0}' """.format(cusg)) 
    coupons=[]
    for cp in parent:
        for cop in cp:
            coupons.append(cop)
    context.coupons=coupons

    

