# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import libs.stdimage.fields
import libs.storages.media_storage
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('attachable_blocks', '0005_auto_20190213_0459'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutBlock',
            fields=[
                ('attachableblock_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to='attachable_blocks.AttachableBlock')),
                ('header', models.CharField(verbose_name='header', max_length=128, blank=True)),
                ('description', models.TextField(verbose_name='description', blank=True)),
                ('link_text', models.CharField(verbose_name='link text', max_length=128, blank=True)),
            ],
            options={
                'verbose_name': 'About block',
                'verbose_name_plural': 'About blocks',
            },
            bases=('attachable_blocks.attachableblock',),
        ),
        migrations.CreateModel(
            name='AboutPageConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=128, blank=True)),
                ('header', models.TextField(verbose_name='Header', max_length=255, null=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('background', libs.stdimage.fields.StdImageField(verbose_name='Background', blank=True, upload_to='', storage=libs.storages.media_storage.MediaStorage('std/background'), aspects='normal', variations={'wide': {'size': (1920, 0), 'crop': False}, 'normal': {'size': (1040, 0), 'crop': False}, 'tablet': {'size': (790, 0), 'crop': False}, 'mobile': {'size': (500, 0), 'crop': False}, 'admin': {'size': (300, 0), 'crop': False}})),
                ('btn_text', models.CharField(verbose_name='Button text', max_length=30, blank=True)),
                ('visible', models.BooleanField(verbose_name='Visibility', default=True)),
                ('updated', models.DateTimeField(verbose_name='change date', auto_now=True)),
                ('text', ckeditor.fields.CKEditorUploadField(verbose_name='Content page', blank=True, help_text='Image sizes: from <b>800x450</b> to <b>1024x576</b>')),
            ],
            options={
                'verbose_name': 'Settings',
                'abstract': False,
                'default_permissions': ('change', 'add'),
            },
        ),
    ]
