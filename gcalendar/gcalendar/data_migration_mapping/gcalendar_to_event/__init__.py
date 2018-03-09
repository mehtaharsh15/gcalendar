#!/usr/bin/env python
# -*- coding: utf-8 -*-
import frappe

def pre_process(events):
	if events["status"] == "cancelled":
		if frappe.db.exists("Event", dict(gcalendar_sync_id=events["id"])):
			e = frappe.get_doc("Event", dict(gcalendar_sync_id=events["id"]))
			frappe.delete_doc("Event", e.name)
		return {}

	elif events["status"] == "confirmed":
		if 'date' in events["start"]:
			datevar = 'date'
		else:
			datevar = 'dateTime'


		event = {
			'id': events["id"],
			'summary': events["summary"],
			'start_datetime': events["start"][datevar],
			'end_datetime': events["end"][datevar]
		}

		if 'description' in events:
			event.update({'description': events["description"]})
		else:
			event.update({'description': ""})

		if datevar == 'date':
			event.update({'all_day': 1})

		return event
