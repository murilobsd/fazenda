# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Fazenda(models.Model):
    '''
    Classe para instanciar as Fazendas
    
    # Criando a Fazenda do Murilo
    >>> fazenda_m = Fazenda.objects.create(nome="Fazenda do Murilo", area_integral='123.45', arean_cultivada='0.00')
    >>> fazenda_m.nome
    Fazenda do Murilo
    >>> fazenda_m
    Fazenda do Murilo
    '''
    usuario         = models.ForeignKey(User)
    nome            = models.CharField(max_length=200)
    slug            = models.SlugField(max_length=200)
    area_integral   = models.DecimalField(max_digits=10, decimal_places=2) # Área Integra
    arean_cultivada = models.DecimalField(max_digits=10, decimal_places=2) # Área Não Cultivada
    criacao         = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-criacao']
            
    def __unicode__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('fazenda', None, [str(self.slug)])
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.nome)
        super(Fazenda, self).save(*args, **kwargs)

class Ciclo(models.Model):
    '''
    Classe para instanciar os Ciclos
    a cada um ano surge um ciclo novo
    
    # Criando um ciclo ?
    >>> ciclo_atual = Ciclo.objects.create(nome='2013', fazenda='fazenda_m')
    '''
    
    usuario = models.ForeignKey(User) # Sera que realmente eh necessario usuario em todas as Models?
    criacao = models.DateTimeField(auto_now_add=True)
    nome    = models.CharField(max_length=200) # Ciclo 2013, 2014...
    fazenda = models.ForeignKey(Fazenda)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome
        
class Zona(models.Model):
    '''
    Classe para instanciar os Talhoes
    
    # Criando uma Zona
    >>> zona1 = Zona.objects.create(nome='1')
    >>> zona1.nome
    1
    '''
    
    usuario = models.ForeignKey(User)
    criacao = models.DateTimeField(auto_now_add=True)
    nome    = models.CharField(max_length=200) # Zona 1, Zona 2
    ciclo   = models.ForeignKey(Ciclo)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome

class Variedade(models.Model):
    '''
    Classe para instanciar as Variedades de Cana
    '''
    
    usuario = models.ForeignKey(User)
    criacao = models.DateTimeField(auto_now_add=True)
    nome    = models.CharField(max_length=200) # RFB1298, RB1872827 ...
    fazenda = models.ForeignKey(Fazenda)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome

class TipoProduto(models.Model):
    '''
    Classe para instanciar os Tipos de 
    Produto Adubo, Inseticida...
    '''
    
    usuario = models.ForeignKey(User)
    criacao = models.DateTimeField(auto_now_add=True)
    nome    = models.CharField(max_length=200) # RFB1298, RB1872827 ...
    fazenda = models.ForeignKey(Fazenda)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome

class Produto(models.Model):
    '''
    Classe para instanciar os Produtos
    '''
    
    UNIDADES = (
        ('K', 'Kilograma'),
        ('G', 'Gramas'),
        ('L', 'Litros'),
        ('M', 'Mililitros')
    )
    
    usuario         = models.ForeignKey(User)
    criacao         = models.DateTimeField(auto_now_add=True)
    nome            = models.CharField(max_length=200)
    tipo_produto    = models.ForeignKey(TipoProduto)
    unidade         = models.CharField(max_length=2, choices=UNIDADES)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome
        
class Tabela(models.Model):
    '''
    Classe que instancia as Tabelas
    '''
    
    usuario     = models.ForeignKey(User)
    criacao     = models.DateTimeField(auto_now_add=True)
    nome        = models.CharField(max_length=200) # Tabela 1, Tabela 2
    zona        = models.ForeignKey(Zona)
    area        = models.DecimalField(max_digits=10, decimal_places=2)
    area_muda   = models.DecimalField(max_digits=10, decimal_places=2)
    area_moagem = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    variedade   = models.ForeignKey(Variedade)
    corte       = models.CharField(max_length=100)
    arquivo     = models.FileField(upload_to='gps/%d/%m/%Y', blank=True)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.area_moagem = self.area - self.area_muda
        super(Tabela, self).save(*args, **kwargs)

class Aplicacao(models.Model):
    '''
    Classe para instanciar todas as aplicacoes
    que serao realizadas nas tabelas
    '''
    
    TIPO_CANA = (
        ('P', 'Cana Planta'),
        ('S', 'Cana Soca')
    )
    
    usuario     = models.ForeignKey(User)
    criacao     = models.DateTimeField(auto_now_add=True)
    tabela      = models.ForeignKey(Tabela)
    data        = models.DateField()
    produto     = models.ForeignKey(Produto)
    quantidade  = models.DecimalField(max_digits=10, decimal_places=2)
    unidade     = models.CharField(max_length=1, choices=TIPO_CANA)
    total       = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return "%s - %s" % (self.tabela, self.produto)

class GPSData(models.Model):
    '''
    Classe para instanciar os dados de latitude e longitude
    de cada tabela da Zona.
    '''
    
    tabela          = models.ForeignKey(Tabela)
    lon_posicao     = models.DecimalField(max_digits=8, decimal_places=3)
    lat_posicao     = models.DecimalField(max_digits=8, decimal_places=3)
    
    def __unicode__(self):
        return "%s: %s %s" % (self.tabela, self.lon_posicao, self.lat_posicao)