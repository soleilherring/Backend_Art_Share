# Generated by Django 4.1.5 on 2023-02-08 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0028_alter_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
