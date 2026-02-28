from django.db import migrations, models


def rebrand_outerwear(apps, schema_editor):
    SiteSettings = apps.get_model('store', 'SiteSettings')
    Category = apps.get_model('store', 'Category')

    for site in SiteSettings.objects.all():
        site.nav_streetwear_en = 'Outerwear'
        site.nav_streetwear_ar = 'ملابس خارجية'
        site.nav_streetwear_fr = 'Outerwear'
        site.ticker_items_en = (site.ticker_items_en or '').replace('STREETWEAR', 'OUTERWEAR').replace('Streetwear', 'Outerwear')
        site.ticker_items_ar = (site.ticker_items_ar or '').replace('ستريت وير', 'ملابس خارجية')
        site.footer_tagline_en = (site.footer_tagline_en or '').replace('Streetwear', 'Outerwear')
        site.footer_tagline_fr = (site.footer_tagline_fr or '').replace('Streetwear', 'Outerwear')
        site.save(update_fields=[
            'nav_streetwear_en', 'nav_streetwear_ar', 'nav_streetwear_fr',
            'ticker_items_en', 'ticker_items_ar', 'footer_tagline_en', 'footer_tagline_fr',
        ])

    # Rename legacy streetwear category to outerwear where possible.
    for cat in Category.objects.filter(slug='streetwear'):
        cat.name_en = 'Outerwear'
        cat.name_ar = 'ملابس خارجية'
        cat.name_fr = 'Outerwear'
        if not Category.objects.filter(slug='outerwear').exclude(id=cat.id).exists():
            cat.slug = 'outerwear'
        cat.save(update_fields=['name_en', 'name_ar', 'name_fr', 'slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_model_3d_lookbookitem_model_3d'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='ticker_items_en',
            field=models.CharField(default='MOONBLOCK,OUTERWEAR,GYM WEAR,SS 2026,MOVE BY NIGHT', max_length=500),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='ticker_items_ar',
            field=models.CharField(blank=True, default='مونبلوك,ملابس خارجية,ملابس جيم,SS 2026,تحرك في الليل', max_length=500),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='footer_tagline_en',
            field=models.CharField(default='Outerwear and gym wear for those who move by night and grind by day.', max_length=300),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='footer_tagline_fr',
            field=models.CharField(blank=True, default='Outerwear et tenue de gym pour ceux qui bougent la nuit et travaillent le jour.', max_length=300),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='nav_streetwear_en',
            field=models.CharField(default='Outerwear', max_length=50),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='nav_streetwear_ar',
            field=models.CharField(blank=True, default='ملابس خارجية', max_length=50),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='nav_streetwear_fr',
            field=models.CharField(blank=True, default='Outerwear', max_length=50),
        ),
        migrations.RunPython(rebrand_outerwear, migrations.RunPython.noop),
    ]
