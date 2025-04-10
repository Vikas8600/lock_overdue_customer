from erpnext.accounts.report.accounts_receivable_summary.accounts_receivable_summary import execute 
import frappe

from datetime import datetime

# for version-15
# def check_overdue_customer():
#     selling_settings = frappe.get_doc("Selling Settings")
#     no = selling_settings.custom_lock_customer_transactions_with_overdue_for_more_than
#     if no == 0: return
#     print("check overdue customer")
#     customers = frappe.db.get_list("Customer",{"disabled":0},pluck='name')
#     print("customers",customers)
#     filters={
# 	'report_date':datetime.now(),
# 	'ageing_based_on' :"Due Date" ,
# 	'range' : str(no),
# 	'party_type' : 'Customer',
# 	'party' :customers,
# 	'based_on_payment_terms' : '1',
# 	 }
#     print("filters",filters)
#     data=execute(filters)
#     if data:
#       print("report data",data[1],no)
#       for i in data[1]:
#         print("i",i)
#         doc = frappe.get_doc("Customer",i['party'])
#         if i[f"range2"] > 0:
#           doc.is_frozen = 1
#         else:
#           doc.is_frozen = 0
#         doc.save()


# for version-14
def check_overdue_customer():
    selling_settings = frappe.get_doc("Selling Settings")
    no = selling_settings.custom_lock_customer_transactions_with_overdue_for_more_than
    if no == 0: return
    print("check overdue customer")
    customers = frappe.db.get_list("Customer",{"disabled":0},pluck='name')
    print("customers",customers)
    filters={
	'report_date':datetime.now(),
	'ageing_based_on' :"Due Date" ,
	'range1' : str(no),
	'range2' : str(no),
	'range3' : str(no),
	'range4' : str(no),
	'party_type' : 'Customer',
	'party' :customers,
	'based_on_payment_terms' : '1',
	 }
    print("filters",filters)
    data=execute(filters)
    if data:
      print("report data",data[1],no)
      for i in data[1]:
          print("i",i)
          if i[f"range5"] > 0:
            frappe.db.set_value("Customer",i['party'],"is_frozen",1,update_modified=False)
          else:
            frappe.db.set_value("Customer",i['party'],"is_frozen",0,update_modified=False)
	# commented this one out because if their document consists of error or missing field or anything it wont work
        # doc = frappe.get_doc("Customer",i['party'])
        # if i[f"range5"] > 0:
        #   doc.is_frozen = 1
        # else:
        #   doc.is_frozen = 0
        # doc.save()
