import client


def test_programmer_count():
    assert client.get_programmer_count() == 7


def test_programmer_by_id():
    assert client.get_programmer_by_id(999)['first'] == 'Ada'
    assert client.get_programmer_by_id(997)['first'] == 'Niklaus'


def test_programmer_by_invalid_id():
    result = client.get_programmer_by_id(1)
    assert (result is None) or (result == {})


def test_programmer_has_all_required_fields():
    keys = ['born', 'first', 'last', 'id', 'location']
    programmer = client.get_programmer_by_id(999)
    assert all(k in programmer for k in keys)


def test_get_full_name_from_first():
    assert client.get_full_name_from_first('Ada') == 'Ada Lovelace'
    assert client.get_full_name_from_first('Linus') == 'Linus Torvalds'


def test_get_full_name_from_first_case_insensitive():
    assert client.get_full_name_from_first('ada') == 'Ada Lovelace'
    assert client.get_full_name_from_first('ADA') == 'Ada Lovelace'


def test_get_last_name_from_invalid_first_name():
    assert client.get_full_name_from_first('Homer') is None
