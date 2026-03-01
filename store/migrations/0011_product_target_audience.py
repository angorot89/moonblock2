from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_delete_gymsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='target_audience',
            field=models.CharField(choices=[('all', 'For All'), ('him', 'For Him'), ('her', 'For Her')], default='all', max_length=10, verbose_name='Audience'),
        ),
    ]
