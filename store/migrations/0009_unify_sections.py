from django.db import migrations, models
import django.db.models.deletion
from django.utils.text import slugify


def _unique_slug(Section, base_slug):
    root = base_slug or 'section'
    slug = root
    counter = 2
    while Section.objects.filter(slug=slug).exists():
        slug = f"{root}-{counter}"
        counter += 1
    return slug


def unify_sections(apps, schema_editor):
    Category = apps.get_model('store', 'Category')
    Section = apps.get_model('store', 'OuterwearSection')
    GymSection = apps.get_model('store', 'GymSection')

    outerwear_category = Category.objects.filter(slug='outerwear').first() or Category.objects.filter(slug='streetwear').first()

    for section in Section.objects.all():
        if not section.target_category_id and outerwear_category:
            section.target_category_id = outerwear_category.id
        if not section.slug:
            section.slug = _unique_slug(Section, slugify(section.name_en) or f'section-{section.id}')
        if section.is_active is None:
            section.is_active = True
        section.save(update_fields=['target_category', 'slug', 'is_active'])

    for gym_section in GymSection.objects.all():
        base_slug = slugify(gym_section.name_en) or f'gym-section-{gym_section.id}'
        existing = Section.objects.filter(
            name_en=gym_section.name_en,
            target_category_id=gym_section.target_category_id,
        ).first()
        if existing:
            existing.name_ar = gym_section.name_ar or existing.name_ar
            existing.name_fr = gym_section.name_fr or existing.name_fr
            existing.order = gym_section.order
            existing.is_active = gym_section.is_active
            if not existing.slug:
                existing.slug = _unique_slug(Section, base_slug)
            existing.save(update_fields=['name_ar', 'name_fr', 'order', 'is_active', 'slug'])
            continue

        Section.objects.create(
            name_en=gym_section.name_en,
            name_ar=gym_section.name_ar,
            name_fr=gym_section.name_fr,
            slug=_unique_slug(Section, base_slug),
            target_category_id=gym_section.target_category_id,
            order=gym_section.order,
            is_active=gym_section.is_active,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_gym_sections'),
    ]

    operations = [
        migrations.AddField(
            model_name='outerwearsection',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='outerwearsection',
            name='target_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sections', to='store.category'),
        ),
        migrations.AlterModelOptions(
            name='outerwearsection',
            options={'ordering': ['order', 'name_en'], 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
        ),
        migrations.RunPython(unify_sections, migrations.RunPython.noop),
    ]
