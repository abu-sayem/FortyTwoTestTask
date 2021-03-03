from django.shortcuts import get_object_or_404, render
from django.views import View
from apps.contacts.models import Contact


class ContactView(View):
    template_name = 'contacts/contact.html'

    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Contact, pk=1)
        return render(request, self.template_name, {'data': data})
