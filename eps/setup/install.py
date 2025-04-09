import frappe
from eps.setup.erpnext import create_default_energy_point_rules
def after_install():
    if "erpnext" in frappe.get_installed_apps():
        create_default_energy_point_rules()