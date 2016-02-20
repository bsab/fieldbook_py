Fieldbook_py
------------

A simple python package for interacting with the Fieldbook.com API

PLEASE NOTE: This package is still in development so please use with caution.

To install the package:

    >>> pip install fieldbook_py


To use, simply do:

    >>> import fieldbook_py
    >>> fieldbook = fieldbook_py.FieldbookClient('api_key_here',
                                                 'api_secret_here',
                                                 'fieldbook_url_here')

    >>> all_rows = fieldbook.get_rows('sheet_name')

    >>> print(all_rows)
    >>> new_data = {
            'field_name_1': 'new_value_1',
            'field_name_2': 'new_value_2',
            'field_name_3': 3
        }

    >>> new_row = fieldbook.add_row('sheet_name', new_data)
    >>> print(new_row)

    >>> updated_data = {
            'field_name_2': 'updated_value_2'
        }
    >>> fieldbook.update_row('sheet_name', 3, updated_data)

    >>> fieldbook.delete_row('sheet_name', 3)


