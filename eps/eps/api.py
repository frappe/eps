import frappe


@frappe.whitelist()
def get_point_logs(doctype, docname):
	from eps.eps.doctype.energy_point_settings.energy_point_settings import is_energy_point_enabled

	if not is_energy_point_enabled():
		return []

	return frappe.get_all(
		"Energy Point Log",
		filters={"reference_doctype": doctype, "reference_name": docname, "type": ["!=", "Review"]},
		fields=["*"],
	)


def get_timeline_for_energy_points(doctype, docname):
	energy_points = get_point_logs(doctype, docname)
	timeline_content = []
	for e in energy_points:
		timeline_entry = {
			"log": e,
			"timeline_badge": get_timeline_badge(e.points),
			"creation": e.creation,
			"method": "eps.energy_points.format_form_log(custom_item.log)",
		}
		timeline_content.append(timeline_entry)
	return timeline_content


def get_timeline_badge(log_points):
	badge_class = "appreciation" if log_points > 0 else "criticism"
	badge_html = f'<div class="timeline-badge {badge_class} bold">{log_points}</div>'
	return badge_html
