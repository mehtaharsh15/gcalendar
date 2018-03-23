from __future__ import unicode_literals
import frappe

def remove_syncid_on_duplicates(doc, method):
	if doc.gcalendar_sync_id:
		frappe.db.set_value("Event", doc.name, "gcalendar_sync_id", None)
		frappe.db.commit()
