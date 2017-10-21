from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views as entry_views
urlpatterns = [
	url(r'^(?P<pk1>\d+)/(?P<pk2>\d+)/$',entry_views.chat,name='chat'),
	url(r'^(?P<pk>\d+)/$',entry_views.messages,name='messages'),
]