import frappe

from eps.eps.doctype.energy_point_log.energy_point_log import get_energy_points
from eps.eps.doctype.energy_point_settings.energy_point_settings import (
	is_energy_point_enabled,
)


def extend_bootinfo(bootinfo):
	bootinfo.points = get_energy_points(user=frappe.session.user)
	bootinfo.energy_points_enabled = is_energy_point_enabled()
