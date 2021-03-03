from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

from apps.contacts.models import Log


class RequestLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        log = Log()
        log.path = request.path
        log.method = request.method
        log.user = request.user
        log.time = datetime.now()
        log.browser = request.META.get('HTTP_USER_AGENT')
        log.save()
