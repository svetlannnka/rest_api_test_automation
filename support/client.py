import requests

from support.logger import logger, log_response


class Client:
    DEFAULT_TIMEOUT = 10.0

    def get(self, url, custom_headers=None, timeout=DEFAULT_TIMEOUT):
        response = requests.get(url=url, headers=custom_headers, timeout=timeout)
        return response

    def post(self, url, custom_headers=None, timeout=DEFAULT_TIMEOUT, **payload):
        response = requests.post(url=url, headers=custom_headers, timeout=timeout, json=payload)
        return response

    def put(self, url, custom_headers=None, timeout=DEFAULT_TIMEOUT, **payload):
        response = requests.put(url=url, headers=custom_headers, timeout=timeout, json=payload)
        return response

    def delete(self, url, custom_headers=None, timeout=DEFAULT_TIMEOUT, **payload):
        response = requests.delete(url=url, headers=custom_headers, timeout=timeout, json=payload)
        return response
