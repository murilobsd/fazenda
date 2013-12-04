from django.test import TestCase
from fazenda.gerenciador.forms import RegFarmForm
from fazenda.gerenciador.models import Farm
# Create your tests here.

class FarmDetailTest(TestCase):
    def setUp(self):
        s = Farm.objects.create(name='Fazenda Santa Matilde', full_area=123.45, uncultivated_area=0.00)
        self.resp = self.client.get('/fazenda/%d/' % s.pk)
    
    def test_get(self):
        'GET return code 200'
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        'Detail Template'
        self.assertTemplateUsed(self.resp, 'gerenciador/det_farm.html')
    
    def test_context(self):
        'Context must have a farm instance'
        farm = self.resp.context['farm']
        self.assertIsInstance(farm, Farm)
    
    def test_html(self):
        'Html contains Fazenda Santa Matilde'
        self.assertContains(self.resp, 'Fazenda Santa Matilde')

class FarmDetailNotFound(TestCase):
    
    def test_not_found(self):
        'Not found farm'
        response = self.client.get('/fazenda/0/')
        self.assertEqual(404, response.status_code)