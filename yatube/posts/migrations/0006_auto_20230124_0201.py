# Generated by Django 2.2.6 on 2023-01-23 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20230122_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Текст нового поста', validators=[posts.validators.validate_not_empty], verbose_name='Текст поста'),
        ),
    ]
