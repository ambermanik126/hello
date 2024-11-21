from django.template import loader
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import resolve_url
from django.views.generic import TemplateView
from libs.views import CachedViewMixin
from seo.seo import Seo
from .models import AboutPageConfig


class IndexView(CachedViewMixin, TemplateView):
    template_name = 'about/index.html'
    config = None

    def last_modified(self, *args, **kwargs):
        self.config = AboutPageConfig.get_solo()
        return self.config.updated

    def get(self, request, *args, **kwargs):
        # SEO
        seo = Seo()
        seo.set_data(self.config)
        seo.save(request)

        request.breadcrumbs.add(_('Home'), resolve_url('index'))
        request.breadcrumbs.add(self.config.title, self.config.get_absolute_url())

        return self.render_to_response({
            'config': self.config,
        })


def about_block_render(context, block, **kwargs):
    return loader.render_to_string('about/block.html', {
        'block': block,
    }, request=context.get('request'))
