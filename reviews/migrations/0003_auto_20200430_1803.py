# Generated by Django 3.0.4 on 2020-04-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200430_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_mobile',
            name='image',
            field=models.ImageField(default='', upload_to='reviews/images'),
        ),
    ]