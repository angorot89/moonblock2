from django.db import migrations, models
import django.db.models.deletion


def create_default_outerwear_sections(apps, schema_editor):
    OuterwearSection = apps.get_model('store', 'OuterwearSection')
    defaults = [
        {
            'slug': 'hoodies-sweats',
            'name_en': 'Hoodies & Sweats',
            'name_ar': 'هوديز وسويتس',
            'name_fr': 'Hoodies & Sweats',
            'order': 1,
        },
        {
            'slug': 'pants',
            'name_en': 'Pants',
            'name_ar': 'بناطيل',
            'name_fr': 'Pantalons',
            'order': 2,
        },
        {
            'slug': 'tshirts',
            'name_en': 'T-Shirts',
            'name_ar': 'تيشيرتات',
            'name_fr': 'T-Shirts',
            'order': 3,
        },
    ]
    for row in defaults:
        OuterwearSection.objects.get_or_create(
            slug=row['slug'],
            defaults=row,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_outerwear_rebrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='OuterwearSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100, verbose_name='Name (EN)')),
                ('name_ar', models.CharField(blank=True, max_length=100, verbose_name='Name (AR)')),
                ('name_fr', models.CharField(blank=True, max_length=100, verbose_name='Name (FR)')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Outerwear Section',
                'verbose_name_plural': 'Outerwear Sections',
                'ordering': ['order', 'name_en'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='store.outerwearsection'),
        ),
        migrations.RunPython(create_default_outerwear_sections, migrations.RunPython.noop),
    ]
