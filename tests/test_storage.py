from conpyguration.storage import Storage

storage = Storage[dict]()


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

    assert "key1" in storage
    assert "key2" in storage
    assert "key3" not in storage

    storage.remove_item("key1")
    assert len(storage) == 1
    assert storage.get_keys() == ["key2"]

    storage.clear()
    assert len(storage) == 0
    assert storage.get_keys() == []
