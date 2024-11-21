from django.db import models
from django.shortcuts import resolve_url
from django.utils.translation import ugettext_lazy as _
from solo.models import SingletonModel

from attachable_blocks.models import AttachableBlock
from std_page.models import StdPage
from ckeditor.fields import CKEditorUploadField


class AboutPageConfig(StdPage, SingletonModel):
    text = CKEditorUploadField(_('Content page'), blank=True)

    class Meta(StdPage.Meta):
        pass

    def get_absolute_url(self):
        return resolve_url('about:index')


class AboutBlock(AttachableBlock):
    BLOCK_VIEW = 'about.views.about_block_render'

    header = models.CharField(_('header'), max_length=128, blank=True)
    description = models.TextField(_('description'), blank=True)
    link_text = models.CharField(_('link text'), max_length=128, blank=True)

    class Meta:
        verbose_name = _('About block')
        verbose_name_plural = _('About blocks')
