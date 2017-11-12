from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel
)


class HomePage(Page):
    about = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('about'),
        InlinePanel('slider_images', label="Slider Images"),
    ]

class HomePageGalleryImage(Orderable):
    page = ParentalKey(HomePage, related_name='slider_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]