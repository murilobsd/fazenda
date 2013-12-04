from django.test import TestCase
from datetime import datetime
from fazenda.gerenciador.models import Farm

class GerenciadorTest(TestCase):
    '''
    Tests Gerenciador
    '''
    def setUp(self):
        self.obj = Farm(
            name='Fazenda Santa Matilde',
            full_area='746.40',
            uncultivated_area='0.00'
        )
        
        self.obj1 = Farm(
            name='Fazenda sem uncultivated',
            full_area='123.45'
        )
    
    def test_create_obj(self):
        'Farm must have name, full_area and uncultivated_area'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)
    
    def test_has_created_at(self):
        'Farm must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_unicode(self):
        self.assertEqual(u'Fazenda Santa Matilde', unicode(self.obj))
    
    def test_uncultivated_area_default(self):
        'Uncultivated default value 0.00'
        self.obj1.save()
        self.assertEqual(0.0, self.obj1.uncultivated_area)