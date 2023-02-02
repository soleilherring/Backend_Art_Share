# Generated by Django 4.1.5 on 2023-02-01 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0023_alter_item_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='items',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='posts', to='marketplace.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='condition',
            field=models.CharField(blank=True, default='Unknown', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='postimage',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='marketplace.post'),
        ),
    ]
