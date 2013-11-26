# encoding: utf-8
from django.db import models

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
    
    nome = models.CharField(max_length=200)
    area_integral = models.DecimalField(max_digits=10, decimal_places=2) # Área Integra
    arean_cultivada = models.DecimalField(max_digits=10, decimal_places=2) # Área Não Cultivada
    criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-criacao']
            
    def __unicode__(self):
        return self.nome

class Ciclo(models.Model):
    '''
    Classe para instanciar os Ciclos
    a cada um ano surge um ciclo novo
    
    # Criando um ciclo ?
    >>> ciclo_atual = Ciclo.objects.create(nome='2013', fazenda='') 
    '''
    
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200) # Ciclo 2013, 2014...
    fazenda = models.ForeignKey(Fazenda)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome
        
class Zona(models.Model):
    '''
    Classe para instanciar os Talhoes
    '''
    
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200) # Zona 1, Zona 2
    ciclo = models.ForeignKey(Ciclo)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome

class Variedade(models.Model):
    '''
    Classe para instanciar as Variedades de Cana
    '''
    
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200) # RFB1298, RB1872827 ...
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
    
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200) # RFB1298, RB1872827 ...
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
    
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200)
    tipo_produto = models.ForeignKey(TipoProduto)
    unidade = models.CharField(max_length=2, choices=UNIDADES)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome
        
class Tabela(models.Model):
    '''
    Classe que instancia as Tabelas
    '''
    
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=200) # Tabela 1, Tabela 2
    zona = models.ForeignKey(Zona)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    area_muda = models.DecimalField(max_digits=10, decimal_places=2)
    area_moagem = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    variedade = models.ForeignKey(Variedade)
    corte = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            # Prestar atencao aqui e ver se realmente é possivel fazer essa conta
            # A area da moagem = area - area_muda
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
    
    criacao = models.DateTimeField(auto_now_add=True)
    tabela = models.ForeignKey(Tabela)
    data = models.DateField()
    produto = models.ForeignKey(Produto)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    unidade = models.CharField(max_length=1, choices=TIPO_CANA)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['-criacao']
        
    def __unicode__(self):
        return "%s - %s" % (self.tabela, self.produto)

class GpsTabela(Tabela):
    '''
    Classe que salva os dados de GPS de cada Tabela
    '''
    pass
    #arquivo = models.FileField(upload_to='')
    
    # Antes de salvar essa model, preciso pegar o arquivo gerado pelo gps
    # geralmente um xml como é o caso do Garmin, obter os dados de 
    # latitude e longitude de determinada tabela e por fim salvar
    # os pontos dessa coordenada!
    