from django.shortcuts import get_object_or_404, render
from apps.contacts.models import Contact, Log
from apps.contacts.forms import EditForm
from django.views import View
from django.http import JsonResponse
from django.core.serializers import serialize


class ContactView(View):
    template_name = 'contacts/contact.html'

    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Contact, pk=1)
        count = Log.objects.all().count()
        if request.is_ajax():
            context = {
                'data': serialize('json', [data]),
                'count': count,
            }
            return JsonResponse(context, safe=False)
        return render(request, self.template_name, {'data': data, 'count': count})


class LogView(View):
    template_name = 'contacts/log.html'

    def get(self, request, *args, **kwargs):
        data = Log.objects.all().order_by('-id')[:10].values()
        if request.is_ajax():
            data_list = list(data)
            context = {
                'data': data_list,
            }
            return JsonResponse(context, safe=False)
        return render(request, self.template_name, {'data': data})


class EditView(View):
    template_name = 'contacts/edit_contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LoginView(View):
    template_name = 'contacts/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
