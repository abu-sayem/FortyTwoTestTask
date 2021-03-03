from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from apps.contacts.models import Contact


class ContactView(View):
    template_name = 'contacts/contact.html'

    def get(self, request, *args, **kwargs):
        try:
            data = Contact.objects.get(pk=1)
        except Contact.DoesNotExist:
            return render(request, '404.html')
        return render(request, self.template_name, {'data': data})


class LogView(TemplateView):
    template_name = 'contacts/log.html'
