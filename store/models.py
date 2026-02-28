from django.db import models
from django.utils.text import slugify


# ─── LANGUAGE / TRANSLATION HELPERS ──────────────────────────────────────────

LANG_CHOICES = [('en', 'English'), ('ar', 'Arabic'), ('fr', 'French')]


class TranslatedField(models.Model):
    """Mixin: subclass provides translated string fields."""
    class Meta:
        abstract = True


# ─── SITE SETTINGS (singleton) ────────────────────────────────────────────────

class SiteSettings(models.Model):
    # Hero
    hero_eyebrow_en = models.CharField(max_length=200, default='SS 2026 Collection')
    hero_eyebrow_ar = models.CharField(max_length=200, default='مجموعة SS 2026', blank=True)
    hero_eyebrow_fr = models.CharField(max_length=200, default='Collection SS 2026', blank=True)

    hero_title_line1_en = models.CharField(max_length=100, default='MOVE')
    hero_title_line1_ar = models.CharField(max_length=100, default='تحرك', blank=True)
    hero_title_line1_fr = models.CharField(max_length=100, default='BOUGE', blank=True)

    hero_title_line2_en = models.CharField(max_length=100, default='BY')
    hero_title_line2_ar = models.CharField(max_length=100, default='في', blank=True)
    hero_title_line2_fr = models.CharField(max_length=100, default='DE', blank=True)

    hero_title_line3_en = models.CharField(max_length=100, default='NIGHT')
    hero_title_line3_ar = models.CharField(max_length=100, default='الليل', blank=True)
    hero_title_line3_fr = models.CharField(max_length=100, default='NUIT', blank=True)

    hero_subtitle_en = models.CharField(max_length=300, default='Engineered for the grind. Designed for the streets. Where performance meets obsession.')
    hero_subtitle_ar = models.CharField(max_length=300, default='مصمم للصراع. مصنوع للشوارع. حيث الأداء يلتقي الهوس.', blank=True)
    hero_subtitle_fr = models.CharField(max_length=300, default='Conçu pour la lutte. Créé pour les rues. Là où la performance rencontre l\'obsession.', blank=True)

    hero_cta_en = models.CharField(max_length=100, default='Explore Collection')
    hero_cta_ar = models.CharField(max_length=100, default='استكشف المجموعة', blank=True)
    hero_cta_fr = models.CharField(max_length=100, default='Explorer la Collection', blank=True)

    hero_cta2_en = models.CharField(max_length=100, default='View Lookbook')
    hero_cta2_ar = models.CharField(max_length=100, default='عرض اللوك بوك', blank=True)
    hero_cta2_fr = models.CharField(max_length=100, default='Voir le Lookbook', blank=True)

    # Ticker items (comma-separated)
    ticker_items_en = models.CharField(max_length=500, default='MOONBLOCK,OUTERWEAR,GYM WEAR,SS 2026,MOVE BY NIGHT')
    ticker_items_ar = models.CharField(max_length=500, default='مونبلوك,ملابس خارجية,ملابس جيم,SS 2026,تحرك في الليل', blank=True)
    ticker_items_fr = models.CharField(max_length=500, default='MOONBLOCK,VÊTEMENTS DE RUE,TENUE GYM,SS 2026,BOUGER LA NUIT', blank=True)

    # New Arrivals section
    new_arrivals_label_en = models.CharField(max_length=100, default='New Arrivals')
    new_arrivals_label_ar = models.CharField(max_length=100, default='وصل حديثاً', blank=True)
    new_arrivals_label_fr = models.CharField(max_length=100, default='Nouveautés', blank=True)

    new_arrivals_title_en = models.CharField(max_length=100, default='FRESH\nDROPS')
    new_arrivals_title_ar = models.CharField(max_length=100, default='أحدث\nالإصدارات', blank=True)
    new_arrivals_title_fr = models.CharField(max_length=100, default='NOUVELLES\nPIÈCES', blank=True)

    # About section
    about_label_en = models.CharField(max_length=100, default='Our Story')
    about_label_ar = models.CharField(max_length=100, default='قصتنا', blank=True)
    about_label_fr = models.CharField(max_length=100, default='Notre Histoire', blank=True)

    about_title_en = models.CharField(max_length=200, default='BUILT FOR\nTHE RELENTLESS')
    about_title_ar = models.CharField(max_length=200, default='صُنع\nللمثابرين', blank=True)
    about_title_fr = models.CharField(max_length=200, default='FAIT POUR\nLES TENACES', blank=True)

    about_body1_en = models.TextField(default='Moonblock was born in the intersection of athletic discipline and street culture. We create pieces that carry you from pre-dawn training sessions to late-night city runs—without compromise on style or function.')
    about_body1_ar = models.TextField(default='وُلد Moonblock في تقاطع الانضباط الرياضي وثقافة الشارع. نصنع قطعاً تحملك من جلسات التدريب قبل الفجر إلى سباقات المدينة في منتصف الليل—دون تنازل عن الأسلوب أو الوظيفة.', blank=True)
    about_body1_fr = models.TextField(default='Moonblock est né à l\'intersection de la discipline athlétique et de la culture de rue. Nous créons des pièces qui vous portent des sessions d\'entraînement avant l\'aube aux courses nocturnes en ville—sans compromis sur le style ou la fonction.', blank=True)

    about_body2_en = models.TextField(default='Every stitch is intentional. Every silhouette, considered. We don\'t follow trends. We move in cycles—like the moon.')
    about_body2_ar = models.TextField(default='كل غرزة مقصودة. كل صورة ظلية، مدروسة. لا نتبع الاتجاهات. نتحرك في دورات—مثل القمر.', blank=True)
    about_body2_fr = models.TextField(default='Chaque point est intentionnel. Chaque silhouette, réfléchie. Nous ne suivons pas les tendances. Nous nous mouvons en cycles—comme la lune.', blank=True)

    about_cta_en = models.CharField(max_length=100, default='Shop Now')
    about_cta_ar = models.CharField(max_length=100, default='تسوق الآن', blank=True)
    about_cta_fr = models.CharField(max_length=100, default='Acheter Maintenant', blank=True)

    # Stats
    stat1_value = models.CharField(max_length=20, default='4K+')
    stat1_label_en = models.CharField(max_length=50, default='Community')
    stat1_label_ar = models.CharField(max_length=50, default='المجتمع', blank=True)
    stat1_label_fr = models.CharField(max_length=50, default='Communauté', blank=True)

    stat2_value = models.CharField(max_length=20, default='32')
    stat2_label_en = models.CharField(max_length=50, default='Products')
    stat2_label_ar = models.CharField(max_length=50, default='منتج', blank=True)
    stat2_label_fr = models.CharField(max_length=50, default='Produits', blank=True)

    stat3_value = models.CharField(max_length=20, default='100%')
    stat3_label_en = models.CharField(max_length=50, default='No Compromise')
    stat3_label_ar = models.CharField(max_length=50, default='بلا تنازل', blank=True)
    stat3_label_fr = models.CharField(max_length=50, default='Sans Compromis', blank=True)

    # Categories section
    categories_label_en = models.CharField(max_length=100, default='Shop by Category')
    categories_label_ar = models.CharField(max_length=100, default='تسوق حسب الفئة', blank=True)
    categories_label_fr = models.CharField(max_length=100, default='Acheter par Catégorie', blank=True)

    categories_title_en = models.CharField(max_length=100, default='EXPLORE')
    categories_title_ar = models.CharField(max_length=100, default='استكشف', blank=True)
    categories_title_fr = models.CharField(max_length=100, default='EXPLORER', blank=True)

    # Newsletter section
    newsletter_label_en = models.CharField(max_length=100, default='Stay in orbit')
    newsletter_label_ar = models.CharField(max_length=100, default='ابقَ في المدار', blank=True)
    newsletter_label_fr = models.CharField(max_length=100, default='Restez en orbite', blank=True)

    newsletter_title_en = models.CharField(max_length=100, default='JOIN THE BLOCK')
    newsletter_title_ar = models.CharField(max_length=100, default='انضم إلى البلوك', blank=True)
    newsletter_title_fr = models.CharField(max_length=100, default='REJOIGNEZ LE BLOCK', blank=True)

    newsletter_sub_en = models.CharField(max_length=200, default='Early access to drops. Zero spam. Pure Moonblock.')
    newsletter_sub_ar = models.CharField(max_length=200, default='وصول مبكر للإصدارات. لا بريد عشوائي. مونبلوك خالص.', blank=True)
    newsletter_sub_fr = models.CharField(max_length=200, default='Accès anticipé aux drops. Zéro spam. Pur Moonblock.', blank=True)

    # Footer
    footer_tagline_en = models.CharField(max_length=300, default='Outerwear and gym wear for those who move by night and grind by day.')
    footer_tagline_ar = models.CharField(max_length=300, default='ملابس شارع وجيم لمن يتحرك ليلاً ويكد نهاراً.', blank=True)
    footer_tagline_fr = models.CharField(max_length=300, default='Outerwear et tenue de gym pour ceux qui bougent la nuit et travaillent le jour.', blank=True)

    # Social links
    instagram_url = models.URLField(blank=True, default='#')
    tiktok_url = models.URLField(blank=True, default='#')
    twitter_url = models.URLField(blank=True, default='#')

    # Nav
    nav_shop_en = models.CharField(max_length=50, default='Shop')
    nav_shop_ar = models.CharField(max_length=50, default='تسوق', blank=True)
    nav_shop_fr = models.CharField(max_length=50, default='Boutique', blank=True)

    nav_gym_en = models.CharField(max_length=50, default='Gym')
    nav_gym_ar = models.CharField(max_length=50, default='جيم', blank=True)
    nav_gym_fr = models.CharField(max_length=50, default='Gym', blank=True)

    nav_streetwear_en = models.CharField(max_length=50, default='Outerwear')
    nav_streetwear_ar = models.CharField(max_length=50, default='ملابس خارجية', blank=True)
    nav_streetwear_fr = models.CharField(max_length=50, default='Outerwear', blank=True)

    nav_lookbook_en = models.CharField(max_length=50, default='Lookbook')
    nav_lookbook_ar = models.CharField(max_length=50, default='لوك بوك', blank=True)
    nav_lookbook_fr = models.CharField(max_length=50, default='Lookbook', blank=True)

    nav_about_en = models.CharField(max_length=50, default='About')
    nav_about_ar = models.CharField(max_length=50, default='حول', blank=True)
    nav_about_fr = models.CharField(max_length=50, default='À Propos', blank=True)

    nav_shopnow_en = models.CharField(max_length=50, default='Shop Now')
    nav_shopnow_ar = models.CharField(max_length=50, default='تسوق الآن', blank=True)
    nav_shopnow_fr = models.CharField(max_length=50, default='Acheter', blank=True)

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def t(self, field, lang='en'):
        """Get translated value for a field."""
        val = getattr(self, f'{field}_{lang}', None)
        if not val:
            val = getattr(self, f'{field}_en', '')
        return val


# ─── CATEGORY ────────────────────────────────────────────────────────────────

class Category(models.Model):
    name_en = models.CharField(max_length=100, verbose_name='Name (EN)')
    name_ar = models.CharField(max_length=100, blank=True, verbose_name='Name (AR)')
    name_fr = models.CharField(max_length=100, blank=True, verbose_name='Name (FR)')
    slug = models.SlugField(unique=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order', 'name_en']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)

    def name(self, lang='en'):
        return getattr(self, f'name_{lang}', None) or self.name_en

    def __str__(self):
        return self.name_en


class OuterwearSection(models.Model):
    name_en = models.CharField(max_length=100, verbose_name='Name (EN)')
    name_ar = models.CharField(max_length=100, blank=True, verbose_name='Name (AR)')
    name_fr = models.CharField(max_length=100, blank=True, verbose_name='Name (FR)')
    slug = models.SlugField(unique=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Outerwear Section'
        verbose_name_plural = 'Outerwear Sections'
        ordering = ['order', 'name_en']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)

    def name(self, lang='en'):
        return getattr(self, f'name_{lang}', None) or self.name_en

    def __str__(self):
        return self.name_en


# ─── PRODUCT ─────────────────────────────────────────────────────────────────

class Product(models.Model):
    name_en = models.CharField(max_length=200, verbose_name='Name (EN)')
    name_ar = models.CharField(max_length=200, blank=True, verbose_name='Name (AR)')
    name_fr = models.CharField(max_length=200, blank=True, verbose_name='Name (FR)')
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    section = models.ForeignKey(
        OuterwearSection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )

    description_en = models.TextField(blank=True, verbose_name='Description (EN)')
    description_ar = models.TextField(blank=True, verbose_name='Description (AR)')
    description_fr = models.TextField(blank=True, verbose_name='Description (FR)')

    price = models.DecimalField(max_digits=8, decimal_places=2)
    compare_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Main Image')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Image 2 (hover)')
    image3 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Image 3')
    image4 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Image 4')
    image5 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Image 5')
    image6 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Image 6')
    video = models.FileField(upload_to='products/videos/', blank=True, null=True, verbose_name='Short Video')
    model_3d = models.FileField(upload_to='products/models/', blank=True, null=True, verbose_name='3D Model')

    stock = models.PositiveIntegerField(default=0)
    available_sizes = models.CharField(max_length=50, default='S,M,L,XL', help_text='Comma-separated: XS,S,M,L,XL,XXL')

    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name_en)
        super().save(*args, **kwargs)

    def name(self, lang='en'):
        return getattr(self, f'name_{lang}', None) or self.name_en

    def description(self, lang='en'):
        return getattr(self, f'description_{lang}', None) or self.description_en

    def __str__(self):
        return self.name_en

    def get_sizes(self):
        return [s.strip() for s in self.available_sizes.split(',') if s.strip()]

    def is_on_sale(self):
        return self.compare_price and self.compare_price > self.price

    def discount_percent(self):
        if self.is_on_sale():
            return int((1 - self.price / self.compare_price) * 100)
        return 0


# ─── LOOKBOOK ────────────────────────────────────────────────────────────────

class LookbookItem(models.Model):
    title_en = models.CharField(max_length=200, verbose_name='Title (EN)')
    title_ar = models.CharField(max_length=200, blank=True, verbose_name='Title (AR)')
    title_fr = models.CharField(max_length=200, blank=True, verbose_name='Title (FR)')

    caption_en = models.CharField(max_length=400, blank=True, verbose_name='Caption (EN)')
    caption_ar = models.CharField(max_length=400, blank=True, verbose_name='Caption (AR)')
    caption_fr = models.CharField(max_length=400, blank=True, verbose_name='Caption (FR)')

    image = models.ImageField(upload_to='lookbook/', verbose_name='Image')
    model_3d = models.FileField(upload_to='lookbook/models/', blank=True, null=True, verbose_name='3D Model')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Lookbook Item'

    def title(self, lang='en'):
        return getattr(self, f'title_{lang}', None) or self.title_en

    def caption(self, lang='en'):
        return getattr(self, f'caption_{lang}', None) or self.caption_en

    def __str__(self):
        return self.title_en


# ─── ORDER ────────────────────────────────────────────────────────────────────

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'), ('processing', 'Processing'),
        ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default='')
    postal_code = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order #{self.id} — {self.first_name} {self.last_name}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=200)
    size = models.CharField(max_length=10, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.quantity}x {self.product_name}"


# ─── NEWSLETTER ──────────────────────────────────────────────────────────────

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
