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
    url(r'^post/(?P<pk>\d+)/$', entry_views.post_detail, name='post_detail'),
    url(r'^post/new/$', entry_views.post_new, name='post_new'),
    url(r'^login/interests/$',entry_views.interests,name='interests'),
    url(r'^login/upfile/$',entry_views.upfile,name='upfile'),
    url(r'^media//media/documents/(?P<pk>.+)/*$',entry_views.openfile,name='openfile'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)