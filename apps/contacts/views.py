from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from apps.contacts.models import Contact


class ContactView(TemplateView):
    template_name = 'contacts/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_object_or_404(Contact, pk=1)
        return context
