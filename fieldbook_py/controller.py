import requests
import json
import logging

log = logging.getLogger('fieldbook-py')

print("fieldbook_py active")


def alive():
    return "fieldbook_py is alive!"


class FieldbookClient(object):

    def __init__(self, api_key, api_secret, fieldbook_url):

        self.__key = api_key
        self.__secret = api_secret
        self.__url = fieldbook_url
        pass

    def get_rows(self, sheet):
        pass
