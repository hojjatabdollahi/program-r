import requests


class RequestsAPI(object):

    def get(self, url, params):
        return requests.get(url, params=params)
