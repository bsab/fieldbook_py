from context import fieldbook


def get_fieldbook_client():
    return fieldbook.FieldbookClient('','','https://test.fieldbook.url/v1/312f984h3fjgf0i3h4')

class TestClass:

    def test_can_instantiate_instance_of_fieldbookclient(self):
        fbc = get_fieldbook_client()
        assert isinstance(fbc, fieldbook.FieldbookClient)

    def test_patch_url_correctly_formatted(self):
        fbc = get_fieldbook_client()
        result = fbc.get_single_resource_url('test_sheet_name', 33)
        assert result == 'https://test.fieldbook.url/v1/312f984h3fjgf0i3h4/test_sheet_name/33'
