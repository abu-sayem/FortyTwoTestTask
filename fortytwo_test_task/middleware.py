from django.utils.deprecation import MiddlewareMixin

from apps.contacts.models import Log


class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.is_ajax():
            log = Log()
            log.path = request.path
            log.method = request.method
            log.user = request.user
            log.browser = request.META.get('HTTP_USER_AGENT', '')
            log.save()
