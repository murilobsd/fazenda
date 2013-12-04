from django.test import TestCase
from fazenda.gerenciador.forms import RegFarmForm
# Create your tests here.

class GerenciadorTest(TestCase):
    '''
    Tests Gerenciador
    '''
    
    def setUp(self):
        self.resp = self.client.get('/fazenda/cadastrar/')
    
    def test_form_has_fields(self):
        'Form must have 3 fields'
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'full_area', 'uncultivated_area'], form.fields)