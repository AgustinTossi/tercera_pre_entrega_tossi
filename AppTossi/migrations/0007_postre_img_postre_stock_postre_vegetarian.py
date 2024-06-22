# Generated by Django 5.0.6 on 2024-06-14 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTossi', '0006_delete_sugerencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='postre',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='postre',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='postre',
            name='vegetarian',
            field=models.BooleanField(default=False),
        ),
    ]
