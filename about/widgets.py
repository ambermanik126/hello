from django.utils.html import format_html
from libs.widgets import URLWidget
from . import options


class VideoWidget(URLWidget):
    """ Виджет ссылки на видос """

    def render(self, name, value, attrs=None):
        html = super().render(name, value, attrs)
        if value:
            provider, video_key = options.video_parts(value)
            if provider and video_key:
                preview_url = options.video_preview(provider, video_key)
                html = format_html(
                    '<img src="{0}" width="320">{1}',
                    preview_url, html
                )
        return html
