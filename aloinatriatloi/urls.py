"""aloinatriatloi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from taldea import views as taldea_views
from bloga import views as bloga_views
from gertaerak import views as gertaera_views
from django.conf import settings
from django.conf.urls.static import static
from bloga.feeds import LatestEntriesFeed


urlpatterns = [
    url(r'^$', taldea_views.Index.as_view(),name="index"),
    url(r'^taldea/$', taldea_views.Taldea.as_view(),name="taldea"),
    url(r'^berriak/$', bloga_views.PostList.as_view(),name="blog"),
    url(r'^berria/(?P<slug>[-\w/]+)/$', bloga_views.PostView.as_view(), name="post"),
    url(r'^gertaera/(?P<slug>[-\w/]+)/$', gertaera_views.GertaeraView.as_view(), name="gertaera"),
    url(r'^egutegia/$', gertaera_views.Egutegia.as_view(),name="egutegia"),
    url(r'^egutegia/(?P<urtea>[\d]+)/(?P<hilabetea>[\d]+)$', gertaera_views.EgutegiaParam.as_view(),name="egutegiaparam"), 
    url(r'^harremana/$', taldea_views.Harremana.as_view(),name="harremana"),
    url(r'^harremana/bidalita$', taldea_views.Bidalita.as_view(),name="bidalita"),
    url(r'^feed/$', LatestEntriesFeed(), name="feed"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
