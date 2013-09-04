from django.conf.urls import patterns, url
from .views import InventoryList

urlpatterns = patterns('',
    url(r'^inventory/$', InventoryList.as_view()),
)