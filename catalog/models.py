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

class CatalogPage(Page):
    show_in_menus_default = True

    content_panels = Page.content_panels + [
        InlinePanel('products', label="Products"),
        InlinePanel('services', label="Services"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(CatalogPage, self).get_context(request)

        if 'filter' in request.POST:
            filter_text = request.POST.get('filter')
        elif 'filter' in request.GET:
            filter_text = request.GET.get('filter')
        else:
            filter_text = ""

        filtered_products = CatalogPageProduct.objects.filter(
            models.Q(reference__icontains=filter_text) |
            models.Q(name__icontains=filter_text)
        )

        per_page = request.GET.get('per_page')
        if per_page is None:
            default_per_page = CatalogSettings.for_site(request.site).default_per_page
            paginator = Paginator(filtered_products, per_page=default_per_page)
        else:
            paginator = Paginator(filtered_products, per_page=per_page)

        page = request.GET.get('page')
        try:
            paginator.validate_number(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            print('NOT AN INTEGER')
            page = 1
        except EmptyPage:
            print('EMPTY PAGE')
            # If page is out of range (e.g. 9999), deliver last page of results.
            page = paginator.num_pages

        # make the variable 'resources' available on the template
        print(page)
        products = paginator.page(page)
        context['products'] = products

        return context

class CatalogPageService(Orderable):
    page = ParentalKey(CatalogPage, related_name='services')

    name = models.CharField(max_length=255)
    price = models.FloatField()

class CatalogPageProduct(Orderable):
    page = ParentalKey(CatalogPage, related_name='products')

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

    def __str__(self):
        return self.reference + " | " + self.name