# Generated by Django 4.1.5 on 2023-01-27 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_rename_category_item_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='categories',
            new_name='category',
        ),
    ]
