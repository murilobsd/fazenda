from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fazenda.gerenciador.forms import RegFarmForm
from fazenda.gerenciador.models import Farm
from django.shortcuts import get_object_or_404

def registering_farm(request):
    '''
    Registering Farm.
    '''
    if request.method == 'POST':
        return create_farm(request)
    else:
        return new_farm(request)

def new_farm(request):
    return render(request, 'gerenciador/reg_farm.html', {'form': RegFarmForm()})

def create_farm(request):
    form = RegFarmForm(request.POST)
    if not form.is_valid():
        return render(request, 'gerenciador/reg_farm.html', {'form': form})
    
    obj = Farm(**form.cleaned_data)
    obj.save()
    return HttpResponseRedirect('/fazenda/%d/' % obj.pk)

def detail_farm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'gerenciador/det_farm.html', {'farm': farm})