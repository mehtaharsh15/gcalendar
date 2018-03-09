#!/usr/bin/env python
# -*- coding: utf-8 -*-
import frappe

def pre_process(events):
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
