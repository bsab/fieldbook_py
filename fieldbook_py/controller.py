print("fieldbook_py active")


class FieldbookClient(object):

    def __init__(self, api_key, api_secret):

        self.__api_key = api_key
        self.__api_secret = api_secret

        pass

    def get_rows(self, sheet):
        pass