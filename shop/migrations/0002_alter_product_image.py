# Generated by Django 3.2.9 on 2022-01-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='products/%Y/%m/%d'),
        ),
    ]
