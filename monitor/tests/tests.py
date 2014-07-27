from django.test import TestCase

# Create your tests here.

class MonitorTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_run_testsuite(self):
        '''
        python manage.py test monitor.tests.tests.MonitorTest.test_run_testsuite
        '''
        print 'in tests'
        self.assertEquals(1, 1)
        self.assertEquals(2, 2)
