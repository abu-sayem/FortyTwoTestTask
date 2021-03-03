from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView
from apps.contacts.models import Contact, Log
from django.views import View
from django.http import JsonResponse


class ContactView(TemplateView):
    template_name = 'contacts/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_object_or_404(Contact, pk=1)
        return context


class LogView(View):
    template_name = 'contacts/log.html'

    def get(self, request, *args, **kwargs):
        data = Log.objects.all().order_by('-id')[:10].values()
        if request.is_ajax():
            count = Log.objects.all().count()
            data_list = list(data)
            context = {
                'data': data_list,
                'count': count,
            }
            return JsonResponse(context, safe=False)
        return render(request, self.template_name, {'data': data})
