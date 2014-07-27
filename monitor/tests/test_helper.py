# -*- coding:utf-8 -*-
from django.test import TestCase

# Create your tests here.

class HelperTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_helper_testsuite(self):
        '''
        python manage.py test monitor.tests.test_helper.HelperTest.test_helper_testsuite
        '''
        print 'in helper'
        self.assertEquals(1, 1)
        self.assertEquals(2, 2)
