from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings, Category, Product, LookbookItem,
    Order, OrderItem, NewsletterSubscriber
)


# ─── SITE SETTINGS ───────────────────────────────────────────────────────────

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🌐 Social Media Links', {
            'fields': ('instagram_url', 'tiktok_url', 'twitter_url'),
        }),
        ('🧭 Navigation Labels', {
            'fields': (
                ('nav_shop_en', 'nav_shop_ar', 'nav_shop_fr'),
                ('nav_gym_en', 'nav_gym_ar', 'nav_gym_fr'),
                ('nav_streetwear_en', 'nav_streetwear_ar', 'nav_streetwear_fr'),
                ('nav_lookbook_en', 'nav_lookbook_ar', 'nav_lookbook_fr'),
                ('nav_about_en', 'nav_about_ar', 'nav_about_fr'),
                ('nav_shopnow_en', 'nav_shopnow_ar', 'nav_shopnow_fr'),
            ),
            'classes': ('collapse',),
        }),
        ('🏠 Hero Section', {
            'fields': (
                ('hero_eyebrow_en', 'hero_eyebrow_ar', 'hero_eyebrow_fr'),
                ('hero_title_line1_en', 'hero_title_line1_ar', 'hero_title_line1_fr'),
                ('hero_title_line2_en', 'hero_title_line2_ar', 'hero_title_line2_fr'),
                ('hero_title_line3_en', 'hero_title_line3_ar', 'hero_title_line3_fr'),
                ('hero_subtitle_en', 'hero_subtitle_ar', 'hero_subtitle_fr'),
                ('hero_cta_en', 'hero_cta_ar', 'hero_cta_fr'),
                ('hero_cta2_en', 'hero_cta2_ar', 'hero_cta2_fr'),
            ),
        }),
        ('📢 Ticker', {
            'fields': (
                'ticker_items_en', 'ticker_items_ar', 'ticker_items_fr',
            ),
            'description': 'Comma-separated items for the scrolling ticker strip.',
        }),
        ('🆕 New Arrivals Section', {
            'fields': (
                ('new_arrivals_label_en', 'new_arrivals_label_ar', 'new_arrivals_label_fr'),
                ('new_arrivals_title_en', 'new_arrivals_title_ar', 'new_arrivals_title_fr'),
            ),
        }),
        ('📖 About Section', {
            'fields': (
                ('about_label_en', 'about_label_ar', 'about_label_fr'),
                'about_title_en', 'about_title_ar', 'about_title_fr',
                'about_body1_en', 'about_body1_ar', 'about_body1_fr',
                'about_body2_en', 'about_body2_ar', 'about_body2_fr',
                ('about_cta_en', 'about_cta_ar', 'about_cta_fr'),
            ),
        }),
        ('📊 Stats (About Section)', {
            'fields': (
                ('stat1_value', 'stat1_label_en', 'stat1_label_ar', 'stat1_label_fr'),
                ('stat2_value', 'stat2_label_en', 'stat2_label_ar', 'stat2_label_fr'),
                ('stat3_value', 'stat3_label_en', 'stat3_label_ar', 'stat3_label_fr'),
            ),
        }),
        ('📂 Categories Section Labels', {
            'fields': (
                ('categories_label_en', 'categories_label_ar', 'categories_label_fr'),
                ('categories_title_en', 'categories_title_ar', 'categories_title_fr'),
            ),
        }),
        ('📧 Newsletter Section', {
            'fields': (
                ('newsletter_label_en', 'newsletter_label_ar', 'newsletter_label_fr'),
                ('newsletter_title_en', 'newsletter_title_ar', 'newsletter_title_fr'),
                ('newsletter_sub_en', 'newsletter_sub_ar', 'newsletter_sub_fr'),
            ),
        }),
        ('🦶 Footer', {
            'fields': (
                'footer_tagline_en', 'footer_tagline_ar', 'footer_tagline_fr',
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ─── CATEGORY ────────────────────────────────────────────────────────────────

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ar', 'name_fr', 'slug', 'order', 'product_count']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name_en',)}
    fieldsets = (
        ('Category Name (all languages)', {
            'fields': (('name_en', 'name_ar', 'name_fr'), 'slug', 'order'),
        }),
    )

    def product_count(self, obj):
        return obj.products.filter(is_active=True).count()
    product_count.short_description = 'Active Products'


# ─── PRODUCT ────────────────────────────────────────────────────────────────

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'name_en', 'category', 'price', 'stock', 'is_active', 'is_featured', 'is_new']
    list_display_links = ['name_en']
    list_editable = ['price', 'stock', 'is_active', 'is_featured', 'is_new']
    list_filter = ['is_active', 'is_featured', 'is_new', 'category']
    search_fields = ['name_en', 'name_ar', 'name_fr']
    prepopulated_fields = {'slug': ('name_en',)}
    readonly_fields = ['image_preview', 'created_at', 'updated_at']

    fieldsets = (
        ('Product Name (all languages)', {
            'fields': (('name_en', 'name_ar', 'name_fr'), 'slug', 'category'),
        }),
        ('Description (all languages)', {
            'fields': ('description_en', 'description_ar', 'description_fr'),
        }),
        ('Pricing & Stock', {
            'fields': (('price', 'compare_price'), 'stock', 'available_sizes'),
        }),
        ('Images', {
            'fields': ('image_preview', 'image', 'image2', 'image3', 'image4', 'image5', 'image6', 'video', 'model_3d'),
            'description': 'Main image shown in listings. Up to 6 product images in gallery. Optional short video and 3D model on product page.',
        }),
        ('Visibility', {
            'fields': (('is_active', 'is_featured', 'is_new'),),
        }),
        ('Timestamps', {
            'fields': (('created_at', 'updated_at'),),
            'classes': ('collapse',),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:72px;height:72px;object-fit:cover;border-radius:4px;">', obj.image.url)
        return '—'
    image_preview.short_description = 'Preview'


# ─── LOOKBOOK ────────────────────────────────────────────────────────────────

@admin.register(LookbookItem)
class LookbookItemAdmin(admin.ModelAdmin):
    list_display = ['image_preview', 'title_en', 'order', 'is_active', 'created_at']
    list_display_links = ['title_en']
    list_editable = ['order', 'is_active']
    readonly_fields = ['image_preview', 'created_at']

    fieldsets = (
        ('Title (all languages)', {
            'fields': (('title_en', 'title_ar', 'title_fr'),),
        }),
        ('Caption (all languages)', {
            'fields': ('caption_en', 'caption_ar', 'caption_fr'),
        }),
        ('Image & Display', {
            'fields': ('image_preview', 'image', 'model_3d', 'order', 'is_active', 'created_at'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:100px;height:120px;object-fit:cover;border-radius:4px;">', obj.image.url)
        return '—'
    image_preview.short_description = 'Preview'


# ─── ORDERS ──────────────────────────────────────────────────────────────────

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product_name', 'size', 'price', 'quantity', 'subtotal_display']
    fields = ['product_name', 'size', 'price', 'quantity', 'subtotal_display']

    def subtotal_display(self, obj):
        return f"${obj.subtotal():.2f}"
    subtotal_display.short_description = 'Subtotal'

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'total_display', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']
    list_editable = ['status']
    readonly_fields = ['total', 'created_at', 'updated_at']
    inlines = [OrderItemInline]

    fieldsets = (
        ('Customer', {'fields': (('first_name', 'last_name'), 'email', 'phone')}),
        ('Shipping', {'fields': ('address', ('city', 'postal_code'), 'country')}),
        ('Order', {'fields': ('status', 'total', 'notes', ('created_at', 'updated_at'))}),
    )

    def total_display(self, obj):
        return f"${obj.total:.2f}"
    total_display.short_description = 'Total'


@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active']
    readonly_fields = ['subscribed_at']
