import frappe

def execute():
    users = frappe.get_all("User", pluck='name')
    for u in users:
        notification_setting = {
                "user": u,
                "send_email": 0,
                "send_system_notification": 1
        }
        frappe.db.set_value("Energy Point Notification Settings", u, notification_setting)