# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Gcalendar",
			"color": "#4285f4",
			"icon": "octicon octicon-calendar",
			"type": "module",
			"label": _("Google Calendar")
		}
	]
