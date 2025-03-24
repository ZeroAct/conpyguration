from collections import OrderedDict
from typing import Any

store = OrderedDict()


class Storage:
    def add_item(self, key: str, item: Any) -> Any:
        if key in store:
            raise KeyError(f"Key {key} already exists")
        store[key] = item
        return item

    def get_item(self, key: str) -> Any:
        if key not in store:
            raise KeyError(f"Key {key} does not exist")
        return store[key]

    def remove_item(self, key: str) -> Any:
        if key not in store:
            raise KeyError(f"Key {key} does not exist")
        return store.pop(key)

    def get_keys(self) -> list[str]:
        return list(store.keys())

    def clear(self) -> None:
        store.clear()

    def __len__(self) -> int:
        return len(store)

    def __iter__(self):
        return iter(store)


storage = Storage()

__all__ = ["storage"]
