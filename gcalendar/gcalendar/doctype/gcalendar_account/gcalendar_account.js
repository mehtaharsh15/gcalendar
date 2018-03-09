// Copyright (c) 2018, DOKOS and contributors
// For license information, please see license.txt

frappe.ui.form.on('GCalendar Account', {
	/*refresh: function(frm) {
		frm.add_custom_button("Reset remote Calendar", function() {
					frm.set_value("gcalendar_id", "")
					frm.save()
				});
	},*/
	allow_google_access: function(frm) {
			frappe.call({
				method: "gcalendar.gcalendar.doctype.gcalendar_settings.gcalendar_settings.google_callback",
				args: {
					'account': frm.doc.name
				},
				callback: function(r) {
					if(!r.exc) {
						frm.save();
						window.open(r.message.url);
					}
				}
			});
	}
});
