import requests
import json
import logging

log = logging.getLogger('fieldbook-py')

print("fieldbook_py active")


def alive():
    return "fieldbook_py is alive!"


class FieldbookClient(object):

    def __init__(self, api_key, api_secret, sheet_ref):

        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__sheet_ref = sheet_ref
        pass

    def get_rows(self, sheet):
        pass
