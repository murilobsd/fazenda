from django.test import TestCase
from fazenda.gerenciador.forms import RegFarmForm
from fazenda.gerenciador.models import Farm
# Create your tests here.

class GerenciadorTest(TestCase):
    '''
    Tests Gerenciador.
    '''
    
    def setUp(self):
        self.resp = self.client.get('/fazenda/cadastrar/')
    
    def test_get(self):
        'GET / must return status code 200 status.'
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        'Render template.'
        self.assertTemplateUsed(self.resp, 'gerenciador/reg_farm.html')
    
    def test_form_html(self):
        'Test inputs form registering farm.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, '<button')
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"')
    
    def test_csrf(self):
        'html contains csrf'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
    
    def test_has_form(self):
        'context must have the subscription form.'
        form = self.resp.context['form']
        self.assertIsInstance(form, RegFarmForm)

class FarmPostTest(TestCase):
    def setUp(self):
        data = dict(name='Fazenda Santa Matilde', full_area=123.45, uncultivated_area=0.00)
        self.resp = self.client.post('/fazenda/cadastrar/', data)
    
    def test_post(self):
        'Valid Post should redirect to /fazenda/1/.'
        self.assertEqual(302, self.resp.status_code)
    
    def test_save(self):
        'Valid POST must be saved.'
        self.assertTrue(Farm.objects.exists())

class FarmPostInvalidTest(TestCase):
    def setUp(self):
        'String full_area?'
        data = dict(name='Fazenda Invalida', full_area='murilo', uncultivated_area=123.0)
        self.resp = self.client.post('/fazenda/cadastrar/', data)
    
    def test_post(self):
        'Invalid Post should not redirect.'
        self.assertEqual(200, self.resp.status_code)
    
    def test_form_erros(self):
        'Form must be contains errors.'
        self.assertTrue(self.resp.context['form'].errors)
    
    def test_dont_save(self):
        'Do not save data.'
        self.assertFalse(Farm.objects.exists())