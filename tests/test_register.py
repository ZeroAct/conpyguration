import pytest

from conpyguration.registry import get_function_tracker, wrap_function_tracker


def test_wrap_function_tracker():
    def foo(a: int, b: str = "hi") -> int:
        return b + f" {a}"

    wrapped_foo = wrap_function_tracker("foo", foo)
    assert wrapped_foo(3) == "hi 3"

    with pytest.raises(KeyError):
        get_function_tracker("bar")

    tracker = get_function_tracker("foo")
    assert tracker.get("function_name") == "foo"
    assert tracker.get("arguments") == {"a": 3, "b": "hi"}
    assert tracker.get("called_at") is not None
    assert wrapped_foo(**tracker.get("arguments")) == "hi 3"

    with pytest.raises(KeyError):
        wrap_function_tracker("foo", foo)
