Fieldbook_py
------------

A python package for interacting with the Fieldbook.com API

To use (with caution), simply do::

    >>> import fieldbook_py

    >>> print(fieldbook_py.alive())

    >>> fbook = fieldbook_py.FieldbookClient(
            'api_key_here',
            'api_secret_here',
            'fieldbook_url_here')

    >>> rows = fbook.get_rows('sheet_name')

    >>> print(rows)

