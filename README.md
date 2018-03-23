## ERPNext-Google Calendar Integration
Alpha version

#### Installation
This application requires Frappe v10.0.0 or higher.
You can also install it on top of ERPNext.

- bench get-app gcalendar https://github.com/DOKOS-IO/gcalendar
- bench install-app gcalendar
- bench restart && bench migrate

The application is scheduled to run every three minutes by default. Verify that your scheduler is enabled (bench enable-scheduler && bench restart).

Your Frappe site need to have SSL certificates.

#### Configuration

1. Create a new project on Google Cloud Platform and generate new OAuth 2.0 credentials
2. Add `https://{yoursite}` to Authorized JavaScript origins
3. Add `https://{yoursite}?cmd=gcalendar.gcalendar.doctype.gcalendar_settings.gcalendar_settings.google_callback` as an authorized redirect URI
4. Add your Client ID and Client Secret in the Gcalendar application: in "Google Calendar>GCalendar Settings"

5. For each calendar user, create a new calendar account in "Google Calendar>GCalendar Account"  
You should be redirected to a success page

#### Features

1. Creation of a new calendar in Google Calendar  
	- Each user can choose a dedicated name for its Google Calendar.

2. Events sync from ERPNext to GCalendar  
	- All events created in ERPNext are created in Google Calendar.
	- Recurring events are created as recurring events too.

	- Events modified in ERPNext are updated in Google Calendar.

	- Events deleted in ERPNext are deleted in Google Calendar.

3. Events sync from GCalendar to ERPNext  
	- Events created in Google Calendar are created in ERPNext.
	- Events updated in Google Calendar are updated in ERPNext.


#### ToDo and Know Issues

For recurring events, if a single event within a recurring event is deleted in Google Calendar, it will not be deleted on ERPNext side.

If there is an integration error, the event will not be synchronized until you make any change in it (a simple "Save" in Frappe should trigger another synchronization try)

#### License

GPLv3
