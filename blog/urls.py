from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views as entry_views
urlpatterns = [
    url(r'^$', entry_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', entry_views.signup, name='signup'),
    url(r'^post/(?P<pk>\d+)/$', entry_views.post_detail, name='post_detail'),
    url(r'^post/new/$', entry_views.post_new, name='post_new'),
]