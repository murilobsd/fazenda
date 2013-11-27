# encoding: utf-8

from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.template.defaultfilters import slugify
from django.test.client import RequestFactory

from fazenda.core.models import Fazenda
from fazenda.core.views import FazendaDetail

class FazendaTesteCase(TestCase):
    '''
    Simples teste para criacao da fazenda
    '''
    def setUp(self):
        '''
        Criacao da fazenda do Murilo uhuuuu
        Area Integral em Hectares
        Area Nao Cultivada em Hectares
        '''
        self.murilo = User.objects.create(username='murilobsd', password='murilobsd')
        self.muriloslug = Fazenda.objects.create(nome='Murilo Ijanc', usuario=self.murilo, area_integral=123.45, arean_cultivada=0.00)
        self.murilo_fazenda = Fazenda.objects.create(nome='Murilo', usuario=self.murilo, area_integral=123.45, arean_cultivada=0.00)
        self.factory = RequestFactory()
        
    def testeCriacao(self):
        '''
        Realmento criou?
        '''
        self.assertEquals(self.murilo_fazenda.nome, 'Murilo')
        self.assertEquals(self.murilo_fazenda.area_integral, 123.45)
        self.assertEquals(self.murilo_fazenda.arean_cultivada, 0.00)
        self.assertEquals(self.muriloslug.slug, slugify('Murilo Ijanc'))
        self.assertEquals(self.muriloslug.get_absolute_url(), '/fazenda/murilo-ijanc/')
    
    def testeRequisicaoFazenda(self):
        # Requisicoes
        request = self.factory.get(self.muriloslug.get_absolute_url())
        response = FazendaDetail.as_view()(request, slug=self.muriloslug.slug)
        self.assertEqual(response.status_code, 200)
        
    def tearDown(self):
        '''
        Removendo
        '''
        self.murilo_fazenda.delete()
        self.muriloslug.delete()
        self.murilo.delete()