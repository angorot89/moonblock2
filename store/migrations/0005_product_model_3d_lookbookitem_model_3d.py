from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_image4_product_image5_product_image6'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookbookitem',
            name='model_3d',
            field=models.FileField(blank=True, null=True, upload_to='lookbook/models/', verbose_name='3D Model'),
        ),
        migrations.AddField(
            model_name='product',
            name='model_3d',
            field=models.FileField(blank=True, null=True, upload_to='products/models/', verbose_name='3D Model'),
        ),
    ]
