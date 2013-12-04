# coding: utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Farm(models.Model):
    name = models.CharField(max_length=200)
    full_area = models.DecimalField(max_digits=10, decimal_places=2)
    uncultivated_area = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'fazenda')
        verbose_name_plural = _(u'fazendas')
    
    def __unicode__(self):
        return self.name