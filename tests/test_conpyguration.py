import inspect
from typing import Literal, Union

import pytest

from conpyguration.conpy import get_conpyguration
from conpyguration.types import UNDEFINED


def dummy_func_nothing():
    pass


def dummy_func_with_annotations(
    undefined_arg,
    str_arg: str,
    str_arg_with_default: str = "default",
    union_arg: Union[str, int] = "hi",
    literal_arg: Literal[3, "hi"] = 3,
) -> bool:
    return True


def dummy_func_with_annotations_and_docstrings(
    undefined_arg,
    str_arg: str,
    str_arg_with_default: str = "default",
    union_arg: Union[str, int] = "hi",
    literal_arg: Literal[3, "hi"] = 3,
) -> bool:
    """A dummy function with annotations and docstrings

    Args:
        undefined_arg: A description of the argument
        str_arg: A description of the argument
        str_arg_with_default: A description of the argument (default: "default")
        union_arg: A description of the argument (default: "hi")
        literal_arg: A description of the argument (default: 3)

    Returns:
        bool: A description of the return value
    """
    return True


def test_get_conpyguration_nothing():
    conpyguration = get_conpyguration(dummy_func_nothing)
    assert conpyguration == {
        "description": UNDEFINED,
        "module_name": "test_conpyguration",
        "function_name": "dummy_func_nothing",
        "arguments": {},
        "return_spec": UNDEFINED,
    }


def test_get_conpyguration_with_annotations():
    conpyguration = get_conpyguration(dummy_func_with_annotations)
    assert conpyguration.get("description") == UNDEFINED
    assert conpyguration.get("module_name") == "test_conpyguration"
    assert conpyguration.get("function_name") == "dummy_func_with_annotations"
    assert list(conpyguration.get("arguments").keys()) == [
        "undefined_arg",
        "str_arg",
        "str_arg_with_default",
        "union_arg",
        "literal_arg",
    ]
    assert conpyguration.get("arguments").get("undefined_arg") == {
        "value_type": UNDEFINED,
        "default": UNDEFINED,
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("str_arg") == {
        "value_type": str,
        "default": UNDEFINED,
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("str_arg_with_default") == {
        "value_type": str,
        "default": "default",
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("union_arg") == {
        "value_type": (str, int),
        "default": "hi",
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("literal_arg") == {
        "value_type": Literal,
        "default": 3,
        "description": UNDEFINED,
        "choices": (3, "hi"),
    }
    assert conpyguration.get("return_spec") == {
        "value_type": bool,
        "description": UNDEFINED,
    }


def test_get_conpyguration_with_annotations_and_docstrings():
    conpyguration = get_conpyguration(dummy_func_with_annotations_and_docstrings)
    assert conpyguration.get("description") == "A dummy function with annotations and docstrings"
    assert conpyguration.get("module_name") == "test_conpyguration"
    assert conpyguration.get("function_name") == "dummy_func_with_annotations_and_docstrings"
    assert list(conpyguration.get("arguments").keys()) == [
        "undefined_arg",
        "str_arg",
        "str_arg_with_default",
        "union_arg",
        "literal_arg",
    ]
    assert conpyguration.get("arguments").get("undefined_arg") == {
        "value_type": UNDEFINED,
        "default": UNDEFINED,
        "description": "A description of the argument",
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("str_arg") == {
        "value_type": str,
        "default": UNDEFINED,
        "description": "A description of the argument",
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("str_arg_with_default") == {
        "value_type": str,
        "default": "default",
        "description": 'A description of the argument (default: "default")',
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("union_arg") == {
        "value_type": (str, int),
        "default": "hi",
        "description": 'A description of the argument (default: "hi")',
        "choices": UNDEFINED,
    }
    assert conpyguration.get("arguments").get("literal_arg") == {
        "value_type": Literal,
        "default": 3,
        "description": "A description of the argument (default: 3)",
        "choices": (3, "hi"),
    }
    assert conpyguration.get("return_spec") == {
        "value_type": bool,
        "description": "A description of the return value",
    }
