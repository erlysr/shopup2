from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from userprofiles.views import ProfileView, LoginView, PerfilRedirectView, ProfileSignUpView
from popular_topups.views import TopupListView
from stores.views import StoreListView, StoreDetailView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shopup2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^stores/(?P<StoreName>[\w\-]+)/', 'stores.views.StoreView', name='StoreView'),
    url(r'^signup/', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/', 'userprofiles.views.signin', name='signin'),
    url(r'^logout/', 'userprofiles.views.logout_view', name='logout'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^profilesignup/$', ProfileSignUpView.as_view(), name='profilesignup'),

    url(r'^perfil/$', PerfilRedirectView.as_view(url='/signup/'), name='perfil'),    
    url(r'^topups/$', TopupListView.as_view(), name='topup_list'),
    url(r'^topups/(?P<topup>[\w\-]+)/$', TopupListView.as_view(), name='topup_list'),
    url(r'^stores_topups/$', StoreListView.as_view(), name='stores_topups_list'),
    url(r'^stores_topups/(?P<tabulator>[\w\-]+)/$', StoreListView.as_view(), name='stores_topups_list'),
    url(r'^store_detail/(?P<store_name>[\w\-]+)/$', StoreDetailView.as_view(), name='store_detail'),

    
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS

)

urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
)