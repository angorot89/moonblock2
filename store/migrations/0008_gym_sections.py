from django.db import migrations, models
import django.db.models.deletion


def create_default_gym_sections(apps, schema_editor):
    Category = apps.get_model('store', 'Category')
    GymSection = apps.get_model('store', 'GymSection')

    gym_wear = Category.objects.filter(slug='gym-wear').first() or Category.objects.filter(slug='gym').first()
    accessories = Category.objects.filter(slug='accessories').first()

    GymSection.objects.get_or_create(
        name_en='Gym Wear',
        defaults={
            'name_ar': 'ملابس جيم',
            'name_fr': 'Tenue de Gym',
            'target_category': gym_wear,
            'order': 1,
            'is_active': True,
        },
    )
    GymSection.objects.get_or_create(
        name_en='Accessories',
        defaults={
            'name_ar': 'إكسسوارات',
            'name_fr': 'Accessoires',
            'target_category': accessories,
            'order': 2,
            'is_active': True,
        },
    )


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_outerwear_sections'),
    ]

    operations = [
        migrations.CreateModel(
            name='GymSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100, verbose_name='Name (EN)')),
                ('name_ar', models.CharField(blank=True, max_length=100, verbose_name='Name (AR)')),
                ('name_fr', models.CharField(blank=True, max_length=100, verbose_name='Name (FR)')),
                ('order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('target_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gym_sections', to='store.category')),
            ],
            options={
                'verbose_name': 'Gym Section',
                'verbose_name_plural': 'Gym Sections',
                'ordering': ['order', 'name_en'],
            },
        ),
        migrations.RunPython(create_default_gym_sections, migrations.RunPython.noop),
    ]
