# Generated by Django 4.1.5 on 2023-01-26 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_remove_item_category_item_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
