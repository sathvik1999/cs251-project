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
    url(r'^login/upfile/$',	entry_views.upfile,name='upfile'),
    url(r'^login/search/$', entry_views.search, name='search'),
 	url(r'^login/delete/(?P<pk>\d+)/$', entry_views.delete1, name='delete'),
 	url(r'^login/bookpage/(?P<pk>\d+)/$', entry_views.bookpage, name='bookpage'),
 	url(r'^login/reset/$',entry_views.reset,name='reset'),
 	url(r'^login/genre/(?P<pk>\w+)/$',entry_views.genre,name='genre'),
 	url(r'^login/author/(?P<pk>\w+)/$',entry_views.author,name='author'),
 	url(ur'^login/uploader/(?P<pk>\w+)/$',entry_views.uploader,name='uploader'),
 	url(ur'^login/follow/(?P<pk>\w+)/$',entry_views.follow,name='follow'),
 	url(ur'^login/unfollow/(?P<pk>\w+)/$',entry_views.unfollow,name='unfollow'),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)