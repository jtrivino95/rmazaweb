# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.fields import RichTextField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)


@register_setting
class CompanyInfoSettings(BaseSetting):
    """
    Basic key-value relations for being used in any page of the site.
    http://docs.wagtail.io/en/latest/reference/contrib/settings.html
    """
    company_name = models.TextField("Company Name", max_length=255)
    company_cif = models.TextField("Company CIF", max_length=255)
    company_location = models.TextField("Location", max_length=255)
    company_phones = RichTextField()
    company_opening_hours = RichTextField()
    company_facebook_url = models.URLField("Facebook URL", max_length=255)


class FormPage(AbstractEmailForm):
    about = RichTextField()
    thank_you_text = RichTextField()

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('about'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]


class FormField(AbstractFormField):
    """
    Wagtailforms is a module to introduce simple forms on a Wagtail site. It
    isn't intended as a replacement to Django's form support but as a quick way
    to generate a general purpose data-collection form or contact form
    without having to write code. We use it on the site for a contact form. You
    can read more about Wagtail forms at:
    http://docs.wagtail.io/en/latest/reference/contrib/forms/index.html
    """
    page = ParentalKey('FormPage', related_name='form_fields')