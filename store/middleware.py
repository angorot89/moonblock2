from django.shortcuts import redirect


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check query param first, then session
        lang = request.GET.get('lang')
        if lang in ['en', 'ar', 'fr']:
            request.session['lang'] = lang
        lang = request.session.get('lang', 'en')
        request.lang = lang
        response = self.get_response(request)
        return response


class AuthRequiredMiddleware:
    """Require login for storefront pages, while keeping auth/admin/static accessible."""

    EXEMPT_PREFIXES = (
        '/admin/',
        '/login/',
        '/register/',
        '/skip-auth/',
        '/logout/',
        '/lang/',
        '/static/',
        '/media/',
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        if request.user.is_authenticated or request.session.get('guest_allowed') or any(path.startswith(p) for p in self.EXEMPT_PREFIXES):
            return self.get_response(request)

        return redirect(f"/login/?next={path}")
