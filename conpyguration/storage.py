from collections import OrderedDict
from typing import Generic, TypeVar

store = OrderedDict()

T = TypeVar("T", dict)


class Storage(Generic[T]):
    def add_item(self, key: str, item: T) -> T:
        if key in store:
            raise KeyError(f"Key {key} already exists")
        store[key] = item
        return item

    def get_item(self, key: str) -> T:
        if key not in store:
            raise KeyError(f"Key {key} does not exist")
        return store[key]

    def remove_item(self, key: str) -> T:
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

    def __contains__(self, key: str) -> bool:
        return key in store


__all__ = ["Storage"]
