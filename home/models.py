from __future__ import absolute_import, unicode_literals

from django.db import models

from base.models import FormPage
from blog.models import BlogPage

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
)


class HomePage(FormPage):
    about = RichTextField()

    content_panels = FormPage.content_panels + [
        FieldPanel('about'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['offers']  = BlogPage.objects.filter(live=True)
        return context