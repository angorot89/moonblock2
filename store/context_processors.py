from .models import SiteSettings, Category, OuterwearSection, GymSection


def global_context(request):
    cart = request.session.get('cart', {})
    cart_count = sum(item['quantity'] for item in cart.values())
    lang = getattr(request, 'lang', 'en')
    settings = SiteSettings.get()
    categories = Category.objects.all()
    outerwear_sections = OuterwearSection.objects.all()
    gym_sections = GymSection.objects.filter(is_active=True)

    return {
        'cart_count': cart_count,
        'lang': lang,
        'site': settings,
        'all_categories': categories,
        'outerwear_sections': outerwear_sections,
        'gym_sections': gym_sections,
        'is_rtl': lang == 'ar',
    }
