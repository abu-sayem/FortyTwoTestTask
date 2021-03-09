from django.shortcuts import get_object_or_404
from apps.contacts.models import Contact, Log
from django.views import View
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse

from apps.contacts.service import get_json


class ContactView(TemplateView):
    template_name = 'contacts/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = get_object_or_404(Contact, pk=1)
        return context


class LogListView(ListView):
    model = Log
    template_name = 'contacts/log.html'
    context_object_name = 'logs'

    def get_queryset(self):
        return Log.objects.all().order_by('-id')[:10]


class AJAXView(View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            log_required = request.GET.get('logs', False)
            context = get_json(log_required)
            return JsonResponse(context, safe=False)
