from django.shortcuts import render
from django.views import View


class ContactView(View):
    template_name = 'contacts/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
