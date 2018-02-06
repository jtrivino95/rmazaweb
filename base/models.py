# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.fields import RichTextField

from wagtail.contrib.settings.models import BaseSetting, register_setting


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