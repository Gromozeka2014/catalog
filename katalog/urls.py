from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = (
    url(r'^$', views.Profile_list, name='Profile_list'),
    url(r'^search/$', views.Search, name='Search'),
    url(r'^searchPro/$', views.SearchPro, name='SearchPro'),
    url(r'^add/$', views.Profile_add, name='Profile_add'),
    url(r'^profile/(?P<pk>[a-zA-Z0-9_]+)/$', views.Profile_detail, name='Profile_detail'),
    url(r'^kontakts/(?P<pk>[0-9_]+)/$', views.Profile_kontakts, name='Profile_kontakts'),
    url(r'^profile/(?P<pk>[0-9_]+)/edit/$', views.Profile_edit, name='Profile_edit'),
    url(r'^profile/(?P<pk>[0-9_]+)/delete/$', views.Profile_delete, name='Profile_delete'),
)
