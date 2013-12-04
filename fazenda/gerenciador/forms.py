# coding: utf-8

from django import forms
from django.utils.translation import ugettext as _
class RegFarmForm(forms.Form):
    name = forms.CharField(label=_('Nome'), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: Fazenda Santa Matilde'}))
    full_area = forms.DecimalField(label=_(u'Área Integral'), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: 123.45'}))
    uncultivated_area = forms.DecimalField(label=_(u'Área Não Cultivada'), widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: 10.1'}))
    