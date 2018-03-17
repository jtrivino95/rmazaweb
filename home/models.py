from __future__ import absolute_import, unicode_literals
from offers.models import OfferPage
from base.models import FormPage


class HomePage(FormPage):

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['offers'] = OfferPage.objects.live()
        return context
