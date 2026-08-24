from django.utils import timezone
from .models import SiteVisit

class SiteVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Ignore admin, static files, and media
        path = request.path_info
        if not path.startswith('/admin/') and not path.startswith('/static/') and not path.startswith('/media/'):
            try:
                today = timezone.now().date()
                site_visit, created = SiteVisit.objects.get_or_create(date=today)
                site_visit.count += 1
                site_visit.save(update_fields=['count'])
            except Exception:
                pass # Silently ignore race conditions or db locks
            
        response = self.get_response(request)
        return response
