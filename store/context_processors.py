from .models import SiteSettings, Category


def global_context(request):
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())
    lang = getattr(request, 'lang', 'en')
    settings = SiteSettings.get()
    categories = Category.objects.all()

    return {
        'cart_count': cart_count,
        'lang': lang,
        'site': settings,
        'all_categories': categories,
        'is_rtl': lang == 'ar',
    }
