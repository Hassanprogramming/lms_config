import time
import logging
import os
from pathlib import Path

class RequestsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Use the logger configuration from the settings
        self.logger = logging.getLogger('request_logger')

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        try:
            self.log_request_response(request, response, start_time, end_time)
        except Exception as e:
            # Log the error and continue with the response
            self.logger.error(f"Error in logging request-response: {str(e)}")

        return response

    def log_request_response(self, request, response, start_time, end_time):
        try:
            # logging information
            request_method = request.method
            request_url = request.get_full_path()
            request_timestamp = start_time

            response_status_code = response.status_code
            response_timestamp = end_time

            total_time = end_time - start_time

            # logging information to display
            log_message = (
                f"Method: {request_method}, URL: {request_url}, Timestamp: {request_timestamp}, "
                f"Status Code: {response_status_code}, Response Timestamp: {response_timestamp}, "
                f"Total Time Taken: {total_time:.6f} seconds"
            )

            self.logger.info(log_message)
        except Exception as e:
            # Raise a exception to indicate a logging failure
            raise RuntimeError(f"Error in constructing log message: {str(e)}")