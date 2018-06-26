from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
)
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class CatalogSettings(BaseSetting):
    default_per_page = models.IntegerField(default=50)
    default_product_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE,
        related_name='+', null=True, blank=True
    )
    panels = [
        FieldPanel('default_per_page'),
        ImageChooserPanel('default_product_image'),
    ]


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

    def get_context(self, request, *args, **kwargs):
        context = super(ProductIndexPage, self).get_context(request)

        if 'filter' in request.GET:
            filter_text = request.GET.get('filter')
        else:
            filter_text = ""

        context['self'].products = context['self'].products.filter(
            models.Q(reference__icontains=filter_text) |
            models.Q(name__icontains=filter_text)
        )

        return context


class Service(Orderable):
    page = ParentalKey(ServiceIndexPage, related_name='services')

    name = models.CharField(max_length=255, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    units = models.CharField(max_length=100, verbose_name='Unidades')


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
