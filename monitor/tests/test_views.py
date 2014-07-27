# -*- coding:utf-8 -*-
from django.test import TestCase

# Create your tests here.

class ViewTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_view_testsuite(self):
        '''
        python manage.py test monitor.tests.test_views.ViewTest.test_view_testsuite
        '''
        print 'in view'
        self.assertEquals(1, 1)
        self.assertEquals(2, 2)
