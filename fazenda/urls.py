from django.conf.urls import patterns, include, url

from fazenda.core.views import FazendaDetail
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'fazenda.core.views.home', name='home'),
    url(r'^fazenda/(?P<slug>[-_\w]+)/$', FazendaDetail.as_view(), name='fazenda'),
    # Examples:
    # url(r'^$', 'fazenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
