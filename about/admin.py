from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from solo.admin import SingletonModelAdmin
from attachable_blocks.admin import AttachableBlockAdmin
from std_page.admin import StdPageAdmin
from .models import AboutPageConfig, AboutBlock


@admin.register(AboutPageConfig)
class AboutPageConfigAdmin(StdPageAdmin, SingletonModelAdmin):
    fieldsets = StdPageAdmin.fieldsets + (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('text', ),
        }),
    )


@admin.register(AboutBlock)
class AboutBlockAdmin(AttachableBlockAdmin):
    fieldsets = AttachableBlockAdmin.fieldsets + (
        (_('Customization'), {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('header', 'description', 'link_text'),
        }),
    )
