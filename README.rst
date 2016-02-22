============
fieldbook_py
============
------------------------------------------------------------------
A simple Python package for interacting with the Fieldbook.com API
------------------------------------------------------------------

**PLEASE NOTE: This package is still in development so please use with caution.**

.. image:: https://travis-ci.org/mattstibbs/fieldbook_py.svg?branch=master
    :target: https://travis-ci.org/mattstibbs/fieldbook_py
.. image:: https://travis-ci.org/mattstibbs/fieldbook_py.svg?branch=develop
    :target: https://travis-ci.org/mattstibbs/fieldbook_py

Contributing
------------
If you would like to help in any way please dig in! Raise issues, or issue pull requests - anything appreciated!

Getting Started
---------------
To install the package:

    >>> pip install fieldbook_py


To use, simply do:

    >>> import fieldbook_py
    >>> fieldbook = fieldbook_py.FieldbookClient('api_key_here',
                                                 'api_secret_here',
                                                 'fieldbook_url_here')
    >>> returned_rows = fieldbook.get_all_rows('sheet_name')
    >>> print(returned_rows)

If you want to include or exclude certain fields from the response:

    >>> returned_rows = fieldbook.get_all_rows('sheet_name',
                                          include_fields=('field1', 'field3'),
                                          exclude_fields=('field2',))
    >>> print(returned_rows)

To add a new row:

    >>> new_data = {
            'field_name_1': 'new_value_1',
            'field_name_2': 'new_value_2',
            'field_name_3': 3
        }
    >>> new_row = fieldbook.add_row('sheet_name', new_data)
    >>> print(new_row)

To update an existing row:

    >>> updated_data = {
            'field_name_2': 'updated_value_2'
        }
    >>> fieldbook.update_row('sheet_name', 3, updated_data)

To delete an existing row:

    >>> fieldbook.delete_row('sheet_name', 3)

