function setup_energy_point_listeners(){
    frappe.realtime.on("energy_point_alert", (message) => {
        frappe.show_alert(message);
    });
}
setup_energy_point_listeners()