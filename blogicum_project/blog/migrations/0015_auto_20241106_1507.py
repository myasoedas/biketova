# Generated by Django 3.2.16 on 2024-11-06 12:07

import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20241105_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='embed_video_url',
            field=models.URLField(blank=True, help_text='Добавьте ссылку на видео с YouTube или другого сервиса.', max_length=500, null=True, verbose_name='Встраиваемое видео (URL)'),
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, help_text='Загрузите локальный видеофайл в форматах MP4, MOV или AVI.', null=True, upload_to='blogs_videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'], message='Разрешены только видеофайлы форматов MP4, MOV, AVI.')], verbose_name='Локальное видео'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Если установить дату и время в будущем — можно делать отложенные публикации.', verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Текст публикации'),
        ),
    ]
