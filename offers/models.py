# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class OfferIndexPage(Page):
    show_in_menus_default = True

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class OfferPage(Page):
    body = RichTextField(blank=True, null=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL,
        related_name='+', null=True, blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image'),
    ]