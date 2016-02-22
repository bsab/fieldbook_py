from context import fieldbook


class TestClass:

    def test_can_instantiate_instance_of_fieldbookclient(self):
        fbc = fieldbook.FieldbookClient('','','')
        assert isinstance(fbc, fieldbook.FieldbookClient)
