from django.contrib import admin
from apps.contacts.models import Contact, Log

admin.site.register(Contact)
admin.site.register(Log)
