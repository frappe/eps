app_name = "eps"
app_title = "EPS"
app_publisher = "Frappe Technologies"
app_description = "Energy Points System"
app_email = "developers@frappe.io"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "eps",
# 		"logo": "/assets/eps/logo.png",
# 		"title": "eps",
# 		"route": "/eps",
# 		"has_permission": "eps.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/eps/css/eps.css"
# app_include_js = "/assets/eps/js/eps.js"

# include js, css files in header of web template
# web_include_css = "/assets/eps/css/eps.css"
# web_include_js = "/assets/eps/js/eps.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "eps/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "*": "public/js/review.js", 
    "Notification Settings": "public/js/notifcation.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "eps/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "eps.utils.jinja_methods",
# 	"filters": "eps.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "eps.install.before_install"
after_install = "eps.setup.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "eps.uninstall.before_uninstall"
# after_uninstall = "eps.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "eps.utils.before_app_install"
# after_app_install = "eps.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "eps.utils.before_app_uninstall"
# after_app_uninstall = "eps.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "eps.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"*": {
		"on_change": "eps.eps.doctype.energy_point_rule.energy_point_rule.process_energy_points",
	},
	"User":{
		"on_trash": "eps.eps.doctype.energy_point_log.delete_energy_point_logs_for_user",
  		"after_insert": "eps.eps.doctype.energy_point_notification_settings.energy_point_notification_settings.update_settings"
	},
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"daily": ["eps.eps.doctype.energy_point_settings.energy_point_settings.allocate_review_points"],
	"weekly_long": [
		"eps.eps.doctype.energy_point_log.energy_point_log.send_weekly_summary",
	],
	"monthly": ["eps.eps.doctype.energy_point_log.energy_point_log.send_monthly_summary"],
}

# Testing
# -------

# before_tests = "eps.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "eps.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "eps.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["eps.utils.before_request"]
# after_request = ["eps.utils.after_request"]

# Job Events
# ----------
# before_job = ["eps.utils.before_job"]
# after_job = ["eps.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"eps.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


leaderboards = "eps.eps.leaderboard.get_leaderboards"

extend_bootinfo = ["eps.eps.boot.extend_bootinfo"]

app_include_js = ["eps.bundle.js"]
additional_timeline_content = {
	"*": "eps.eps.api.get_timeline_for_energy_points"
}

fixtures = ["Custom Field"]