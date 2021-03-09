from apps.contacts.models import Log


def get_json(log_required):
    logs = Log.objects.all().order_by('-id')[:10].values()
    logs = list(logs)
    count = Log.objects.all().count()
    context = {
        'count': count,
    }
    if log_required:
        context['logs'] = logs
    return context
