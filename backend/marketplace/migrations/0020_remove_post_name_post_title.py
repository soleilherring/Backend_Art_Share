# Generated by Django 4.1.5 on 2023-01-30 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0019_post_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
    ]
