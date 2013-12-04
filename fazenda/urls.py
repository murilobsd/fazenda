from django.conf.urls import patterns, include, url

from fazenda.core.views import Home
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^fazenda/cadastrar/$', 'fazenda.gerenciador.views.registering_farm', name='reg_farm'),
    url(r'^fazenda/(\d+)/$','fazenda.gerenciador.views.detail_farm', name='det_farm'),
    #url(r'^fazenda/(?P<slug>[-_\w]+)/$', FazendaDetail.as_view(), name='fazenda'),
    #url(r'^fazendas/$', FazendaList.as_view(), name='fazendas'),
    #url(r'^fazenda/criar/$', FazendaCriar.as_view(), name='fazenda_criar'),
    # Examples:
    # url(r'^$', 'fazenda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
