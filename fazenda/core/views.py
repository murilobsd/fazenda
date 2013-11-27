# encoding: utf-8

from django.shortcuts import render_to_response
from django.conf import settings
from django.views.generic import DetailView
from fazenda.core.models import Fazenda
from django.shortcuts import get_object_or_404

def home(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('index.html', context)

class FazendaDetail(DetailView):
    ''''
    Detalhes da Fazenda
    '''
    
    model = Fazenda
    context_object_name = 'fazenda'
    template_name = 'fazenda_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(FazendaDetail, self).get_context_data(**kwargs)
        return context