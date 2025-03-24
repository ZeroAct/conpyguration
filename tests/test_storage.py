from conpyguration import storage


def test_storage():
    storage.clear()
    assert len(storage) == 0

    storage.add_item("key1", "value")
    assert len(storage) == 1
    assert storage.get_item("key1") == "value"
    assert storage.get_keys() == ["key1"]

    storage.add_item("key2", "value")
    assert len(storage) == 2
    assert storage.get_keys() == ["key1", "key2"]

    storage.remove_item("key1")
    assert len(storage) == 1
    assert storage.get_keys() == ["key2"]

    storage.clear()
    assert len(storage) == 0
    assert storage.get_keys() == []
