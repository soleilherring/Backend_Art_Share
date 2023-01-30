# Generated by Django 4.1.5 on 2023-01-30 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0016_remove_post_itemid_remove_review_user_item_postid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='postId',
        ),
        migrations.AddField(
            model_name='post',
            name='itemId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplace.item'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]