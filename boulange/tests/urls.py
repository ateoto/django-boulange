"""URLs to run the tests."""
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^boulange/', include('boulange.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
