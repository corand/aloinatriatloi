# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from bloga.models import Post

class LatestEntriesFeed(Feed):
    title = "Aloña Mendi Triatloi Taldea"
    link = "/feed/"
    description = "Aloña Mendi Triatloi Taldearen azkenengo berriak"

    def items(self):
        return Post.objects.order_by('-data')[:10]

    def item_title(self, item):
        return item.izenburua

    def item_description(self, item):
        return item.edukia

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('post', args=[item.slug])