import requests
from django.conf import settings
from django.http import HttpResponse

class ViteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.DEBUG and request.path.startswith(
            ("/@vite", "/@fs", "/@id", "/node_modules")
        ):
            try:
                vite_response = requests.get(
                    f"{settings.VITE_DEV_SERVER_URL}{request.path}"
                )
                return HttpResponse(
                    vite_response.content,
                    status=vite_response.status_code,
                    content_type=vite_response.headers.get("Content-Type"),
                )
            except requests.RequestException:
                pass
        return response
