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
        url = str.format('{0}{1}{2}', self.__url, '/', sheet)
        print(url)

        try:
            request = requests.get(url,
                                   auth=(self.__key, self.__secret))
            return request.json()

        except requests.ConnectionError as e:
            log.error('Cannot connect to Fieldbook')
            log.error(e)

        except Exception as e:
            log.error(e)

    def add_row(self, sheet, new_record):

        url = str.format('{0}{1}{2}', self.__url, '/', sheet)
        print(url)

        request = requests.post(url, auth=(self.__key, self.__secret), json = new_record)
        print(request.status_code)

        result = json.loads(request.text)
        print(result)

        return result

    def update_row(self, sheet, patch_id, patch_record):

        url = str.format('{0}{1}{2}{3}', self.__url, '/', sheet, '/', patch_id)
        print(url)

        request = requests.patch(url, auth=(self.__key, self.__secret), json = patch_record)
        print(request.status_code)

        result = json.loads(request.text)
        print(result)

        return result
