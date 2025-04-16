# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EnergyPointNotificationSettings(Document):
	pass

def is_email_notifcations_enabled(user):
    return frappe.db.get_single.value(
		"Energy Point Notification Settings", user, "send_email"
	)

def is_system_notification_enabled(user):
    return  frappe.db.get_single.value(
		"Energy Point Notification Settings", user, "send_system_notification"
	)

def update_settings(doc, method):
    if not frappe.db.exists("Energy Point Notification Settings",doc.name):
	
        eps_notify_settings = frappe.new_doc("Energy Point Notification Settings")
        eps_notify_settings.name = doc.name
        eps_notify_settings.send_system_notification = 1
        eps_notify_settings.save()