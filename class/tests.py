from django.test import TestCase, RequestFactory
from django.urls import reverse
from .middleware import *

class MiddlewareTestCase(TestCase):
    def setUp(self):
        self.request_factory = RequestFactory()
        self.middleware = RequestsMiddleware(get_response=lambda r: None)

    def test_middleware_logs_request_response(self):
        # Create a sample request
        url = reverse('home')
        sample_request = self.request_factory.get(url)

        # Simulate the middleware processing the request
        middleware_result = self.middleware(sample_request)

        # Verify that the middleware executed without errors
        self.assertIsNone(middleware_result)

        # Check if the log file is created and has the expected log message
        log_file_path = Path(__file__).resolve().parents[1] / 'logs' / 'request_log.log'
        self.assertTrue(log_file_path.is_file())

        with open(log_file_path, 'r') as log_file:
            log_contents = log_file.read()
            self.assertIn('Method:', log_contents)
            self.assertIn('URL:', log_contents)
            self.assertIn('Status Code:', log_contents)
            self.assertIn('Total Time Taken:', log_contents)
