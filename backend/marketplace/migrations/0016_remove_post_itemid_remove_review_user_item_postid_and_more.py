# Generated by Django 4.1.5 on 2023-01-28 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0015_alter_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='itemId',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='postId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='marketplace.post'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewed_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.user'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to='marketplace.user'),
        ),
    ]
