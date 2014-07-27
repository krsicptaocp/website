# -*- coding:utf-8 -*-
from django.test import TestCase

# Create your tests here.

class ModelTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_model_testsuite(self):
        '''
        python manage.py test monitor.tests.test_models.ModelTest.test_model_testsuite
        '''
        print 'in models'
        self.assertEquals(1, 1)
        self.assertEquals(2, 2)
