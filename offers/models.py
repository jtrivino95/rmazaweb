# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class OffersSettings(BaseSetting):
    default_offer_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
        related_name='+', null=True, blank=True
    )
    panels = [
        ImageChooserPanel('default_offer_image'),
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

    subpage_types = []


class OfferIndexPage(Page):
    show_in_menus_default = True

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = [OfferPage]