from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    InlinePanel,
)
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class CatalogSettings(BaseSetting):
    default_per_page = models.IntegerField(default=50)


class ServiceIndexPage(Page):
    show_in_menus_default = True

    content_panels = Page.content_panels + [
        InlinePanel('services', label="Servicios"),
    ]


class ProductIndexPage(Page):
    show_in_menus_default = True

    content_panels = Page.content_panels + [
        InlinePanel('products', label="Productos"),
    ]


class Service(Orderable):
    page = ParentalKey(ServiceIndexPage, related_name='services')

    name = models.CharField(max_length=255, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')


class Product(Orderable):
    page = ParentalKey(ProductIndexPage, related_name='products')

    reference = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    short_description = RichTextField(null=True, blank=True)
    long_description = RichTextField(null=True, blank=True)
    price = models.FloatField()
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
        related_name='+', null=True, blank=True
    )

    panels = [
        FieldPanel('reference'),
        FieldPanel('name'),
        FieldPanel('short_description'),
        FieldPanel('long_description'),
        FieldPanel('price'),
        ImageChooserPanel('image'),
    ]
