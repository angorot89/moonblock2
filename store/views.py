from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import login, logout
from .models import Product, Category, Order, OrderItem, NewsletterSubscriber, SiteSettings, LookbookItem
from .forms import RegisterForm, LoginForm
import json


def get_cart(request):
    return request.session.get('cart', {})

def save_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True


def home(request):
    lang = request.lang
    site = SiteSettings.get()
    new_arrivals = Product.objects.filter(is_active=True, is_new=True)[:5]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'new_arrivals': new_arrivals,
        'categories': categories,
        'lang': lang,
        'site': site,
    })


def shop(request):
    lang = request.lang
    products = Product.objects.filter(is_active=True)
    category_slug = request.GET.get('category')
    sort = request.GET.get('sort', 'new')
    selected_category = None

    if category_slug:
        # Gracefully handle invalid slugs from stale links/bookmarks.
        selected_category = Category.objects.filter(slug=category_slug).first()
        if not selected_category:
            slug_variants = []
            normalized = category_slug.strip().lower()
            if normalized:
                alias_map = {
                    'outerwear': ['streetwear'],
                    'streetwear': ['outerwear'],
                }
                slug_variants.extend([
                    normalized.replace('_', '-'),
                    normalized.replace('-', ''),
                    normalized.replace('_', ''),
                    normalized.split('-')[0],
                    normalized.split('_')[0],
                ])
                slug_variants.extend(alias_map.get(normalized, []))
                for variant in slug_variants:
                    if not variant:
                        continue
                    selected_category = Category.objects.filter(slug=variant).first()
                    if selected_category:
                        break
        if selected_category:
            products = products.filter(category=selected_category)

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name_en')
    else:
        products = products.order_by('-created_at')

    return render(request, 'store/shop.html', {
        'products': products,
        'selected_category': selected_category,
        'sort': sort,
        'lang': lang,
    })


def product_detail(request, slug):
    lang = request.lang
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related': related,
        'lang': lang,
    })


def lookbook(request):
    lang = request.lang
    items = LookbookItem.objects.filter(is_active=True)
    return render(request, 'store/lookbook.html', {
        'items': items,
        'lang': lang,
    })


def sizing_guide(request):
    lang = request.lang
    assistant_mode = request.GET.get('mode', 'sizing')
    return render(request, 'store/sizing_guide.html', {
        'lang': lang,
        'assistant_mode': assistant_mode,
    })


def cart(request):
    lang = request.lang
    cart_data = get_cart(request)
    items = []
    total = 0
    for key, item in cart_data.items():
        product = Product.objects.filter(id=item['product_id']).first()
        if product:
            subtotal = product.price * item['quantity']
            total += subtotal
            items.append({'key': key, 'product': product, 'size': item.get('size', ''), 'quantity': item['quantity'], 'subtotal': subtotal})
    return render(request, 'store/cart.html', {'items': items, 'total': total, 'lang': lang})


@require_POST
def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data.get('product_id')
    size = data.get('size', '')
    quantity = int(data.get('quantity', 1))
    product = get_object_or_404(Product, id=product_id, is_active=True)
    cart_data = get_cart(request)
    key = f"{product_id}_{size}"
    if key in cart_data:
        cart_data[key]['quantity'] += quantity
    else:
        cart_data[key] = {'product_id': product_id, 'size': size, 'quantity': quantity}
    save_cart(request, cart_data)
    total_qty = sum(i['quantity'] for i in cart_data.values())
    return JsonResponse({'success': True, 'cart_count': total_qty})


@require_POST
def update_cart(request):
    data = json.loads(request.body)
    key = data.get('key')
    quantity = int(data.get('quantity', 0))
    cart_data = get_cart(request)
    if quantity <= 0:
        cart_data.pop(key, None)
    elif key in cart_data:
        cart_data[key]['quantity'] = quantity
    save_cart(request, cart_data)
    return JsonResponse({'success': True})


@require_POST
def remove_from_cart(request):
    data = json.loads(request.body)
    cart_data = get_cart(request)
    cart_data.pop(data.get('key'), None)
    save_cart(request, cart_data)
    return JsonResponse({'success': True})


def checkout(request):
    lang = request.lang
    cart_data = get_cart(request)
    if not cart_data:
        return redirect('cart')
    items = []
    total = 0
    for key, item in cart_data.items():
        product = Product.objects.filter(id=item['product_id']).first()
        if product:
            subtotal = product.price * item['quantity']
            total += subtotal
            items.append({'key': key, 'product': product, 'size': item.get('size', ''), 'quantity': item['quantity'], 'subtotal': subtotal})

    if request.method == 'POST':
        order = Order.objects.create(
            first_name=request.POST.get('first_name', ''),
            last_name=request.POST.get('last_name', ''),
            email=request.POST.get('email', ''),
            phone=request.POST.get('phone', ''),
            address=request.POST.get('address', ''),
            city=request.POST.get('city', ''),
            postal_code=request.POST.get('postal_code', ''),
            country=request.POST.get('country', ''),
            notes=request.POST.get('notes', ''),
            total=total,
        )
        for item in items:
            OrderItem.objects.create(
                order=order, product=item['product'],
                product_name=item['product'].name(lang),
                size=item['size'], price=item['product'].price,
                quantity=item['quantity'],
            )
        request.session['cart'] = {}
        request.session.modified = True
        return redirect('order_success', order_id=order.id)

    return render(request, 'store/checkout.html', {'items': items, 'total': total, 'lang': lang})


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'store/order_success.html', {'order': order, 'lang': request.lang})


@require_POST
def newsletter_subscribe(request):
    email = request.POST.get('email', '').strip()
    if email:
        _, created = NewsletterSubscriber.objects.get_or_create(email=email)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def set_language(request, lang):
    if lang in ['en', 'ar', 'fr']:
        request.session['lang'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"Welcome {user.first_name or user.username}!")
        return redirect('home')

    return render(request, 'store/auth_register.html', {
        'form': form,
        'lang': request.lang,
    })


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm(request, data=request.POST or None)
    next_url = request.GET.get('next') or request.POST.get('next')
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f"Hey {user.first_name or user.username}")
        if next_url and next_url.startswith('/'):
            return redirect(next_url)
        return redirect('home')

    return render(request, 'store/auth_login.html', {
        'form': form,
        'next': next_url or '',
        'lang': request.lang,
    })


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out.")
    return redirect(request.META.get('HTTP_REFERER', '/'))


def skip_auth_view(request):
    request.session['guest_allowed'] = True
    next_url = request.GET.get('next')
    if next_url and next_url.startswith('/'):
        return redirect(next_url)
    return redirect('home')
