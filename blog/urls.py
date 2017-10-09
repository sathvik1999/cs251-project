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
    url(r'^login/advertise/$',	entry_views.advertise,name='advertise'),
    url(r'^login/createcommunity/$',entry_views.community,name='community'),
    url(r'^login/search/$', entry_views.search, name='search'),
 	url(r'^login/delete/(?P<pk>\d+)/$', entry_views.delete1, name='delete'),
 	url(r'^login/deletead/(?P<pk>\d+)/$', entry_views.delete1ad, name='deletead'),
 	url(r'^login/bookpage/(?P<pk>\d+)/$', entry_views.bookpage, name='bookpage'),
 	url(r'^login/adpage/(?P<pk>\d+)/$', entry_views.adpage, name='adpage'),
 	url(r'^login/cpage/(?P<pk>\d+)/$', entry_views.cpage, name='cpage'),
 	url(r'^login/bookpage/change/(?P<pk>\d+)/$', entry_views.change, name='change'),
 	url(r'^login/reset/$',entry_views.reset,name='reset'),
 	url(r'^login/genre/(?P<pk>\w+)/$',entry_views.genre,name='genre'),
 	url(r'^login/author/(?P<pk>\w+)/$',entry_views.author,name='author'),
 	url(r'^login/uploader/(?P<pk>\w+)/$',entry_views.uploader,name='uploader'),
 	url(r'^login/follow/(?P<pk>\w+)/$',entry_views.follow,name='follow'),
 	url(r'^login/unfollow/(?P<pk>\w+)/$',entry_views.unfollow,name='unfollow'),
 	url(r'^login/srequest/(?P<pk>\w+)/$',entry_views.srequest,name='srequest'),
 	url(r'^login/crequest/(?P<pk>\w+)/$',entry_views.crequest,name='crequest'),
 	url(r'^login/prequest/(?P<pk>\d+)/$',entry_views.prequest,name='prequest'),
 	url(r'^login/accept/(?P<pk>\d+)/(?P<name>.+)$',entry_views.accept,name='accept'),
 	url(r'^login/acceptread/(?P<pk>\d+)/(?P<pk1>\d+)/$',entry_views.acceptread,name='acceptread'),
 	url(r'^login/upfileinc/(?P<pk>\d+)/$',	entry_views.upfileinc,name='upfileinc'),
    url(r'^login/leave/(?P<pk>\w+)/$',entry_views.leave,name='leave'),    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)