# Generated by Django 4.1.5 on 2023-01-27 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0014_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
