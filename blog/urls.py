from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from . import views as entry_views
urlpatterns = [
    url(r'^$', entry_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', entry_views.signup, name='signup'),
    url(r'^login/interests/$',entry_views.interests,name='interests'),
    url(r'^login/upfile/$',entry_views.upfile,name='upfile'),
    url(r'^login/search/$', entry_views.search, name='search'),
 	url(r'^login/delete/(?P<pk>\d+)/$', entry_views.delete1, name='delete'),
 	url(r'^login/bookpage/(?P<pk>\d+)/$', entry_views.bookpage, name='bookpage'),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)