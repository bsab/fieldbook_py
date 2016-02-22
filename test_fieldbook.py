from fieldbook_py import fieldbook


def test_can_instantiate_instance_of_fieldbookclient():
    fbc = fieldbook.FieldbookClient('','','')
    assert isinstance(fbc, fieldbook.FieldbookClient)
