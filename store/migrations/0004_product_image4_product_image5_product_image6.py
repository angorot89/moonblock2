from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image 4'),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image 5'),
        ),
        migrations.AddField(
            model_name='product',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Image 6'),
        ),
    ]
