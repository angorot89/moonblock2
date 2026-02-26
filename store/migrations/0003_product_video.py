from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_sitesettings_about_body1_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='products/videos/', verbose_name='Short Video'),
        ),
    ]
