import inspect
from typing import Literal, Union

import pytest

from conpyguration.conpy import get_class_conpyguration, get_conpyguration
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


class DummyClassNothing:
    def __init__(self):
        pass

    def foo(self):
        pass


class DummyClassWithAnnotations:
    def __init__(
        self,
        undefined_arg,
        str_arg: str,
        str_arg_with_default: str = "default",
        union_arg: Union[str, int] = "hi",
        literal_arg: Literal[3, "hi"] = 3,
    ):
        pass

    def foo(self, bar: str) -> bool:
        return True


class DummyClassWithAnnotationsAndDocstrings:
    """A dummy class with annotations and docstrings

    Args:
        undefined_arg: A description of the argument
        str_arg: A description of the argument
        str_arg_with_default: A description of the argument (default: "default")
        union_arg: A description of the argument (default: "hi")
        literal_arg: A description of the argument (default: 3)
    """

    def __init__(
        self,
        undefined_arg,
        str_arg: str,
        str_arg_with_default: str = "default",
        union_arg: Union[str, int] = "hi",
        literal_arg: Literal[3, "hi"] = 3,
    ):
        pass

    def foo(self, bar: str) -> bool:
        """A dummy method with annotations and docstrings

        Args:
            bar: A description of the argument

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


def test_get_class_conpyguration_nothing():
    conpyguration = get_class_conpyguration(DummyClassNothing)
    assert conpyguration == {
        "description": UNDEFINED,
        "module_name": "test_conpyguration",
        "class_name": "DummyClassNothing",
        "init_arguments": {},
        "methods": {
            "foo": {
                "description": UNDEFINED,
                "module_name": "test_conpyguration",
                "function_name": "DummyClassNothing.foo",
                "arguments": {},
                "return_spec": UNDEFINED,
            }
        },
    }


def test_get_class_conpyguration_with_annotations():
    conpyguration = get_class_conpyguration(DummyClassWithAnnotations)
    assert conpyguration.get("description") == UNDEFINED
    assert conpyguration.get("module_name") == "test_conpyguration"
    assert conpyguration.get("class_name") == "DummyClassWithAnnotations"
    assert list(conpyguration.get("init_arguments").keys()) == [
        "undefined_arg",
        "str_arg",
        "str_arg_with_default",
        "union_arg",
        "literal_arg",
    ]
    assert conpyguration.get("init_arguments").get("undefined_arg") == {
        "value_type": UNDEFINED,
        "default": UNDEFINED,
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("str_arg") == {
        "value_type": str,
        "default": UNDEFINED,
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("str_arg_with_default") == {
        "value_type": str,
        "default": "default",
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("union_arg") == {
        "value_type": (str, int),
        "default": "hi",
        "description": UNDEFINED,
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("literal_arg") == {
        "value_type": Literal,
        "default": 3,
        "description": UNDEFINED,
        "choices": (3, "hi"),
    }
    assert list(conpyguration.get("methods").keys()) == ["foo"]
    assert conpyguration.get("methods").get("foo") == {
        "description": UNDEFINED,
        "module_name": "test_conpyguration",
        "function_name": "DummyClassWithAnnotations.foo",
        "arguments": {
            "bar": {
                "value_type": str,
                "default": UNDEFINED,
                "description": UNDEFINED,
                "choices": UNDEFINED,
            }
        },
        "return_spec": {"value_type": bool, "description": UNDEFINED},
    }


def test_get_class_conpyguration_with_annotations_and_docstrings():
    conpyguration = get_class_conpyguration(DummyClassWithAnnotationsAndDocstrings)
    assert conpyguration.get("description") == "A dummy class with annotations and docstrings"
    assert conpyguration.get("module_name") == "test_conpyguration"
    assert conpyguration.get("class_name") == "DummyClassWithAnnotationsAndDocstrings"
    assert list(conpyguration.get("init_arguments").keys()) == [
        "undefined_arg",
        "str_arg",
        "str_arg_with_default",
        "union_arg",
        "literal_arg",
    ]
    assert conpyguration.get("init_arguments").get("undefined_arg") == {
        "value_type": UNDEFINED,
        "default": UNDEFINED,
        "description": "A description of the argument",
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("str_arg") == {
        "value_type": str,
        "default": UNDEFINED,
        "description": "A description of the argument",
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("str_arg_with_default") == {
        "value_type": str,
        "default": "default",
        "description": 'A description of the argument (default: "default")',
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("union_arg") == {
        "value_type": (str, int),
        "default": "hi",
        "description": 'A description of the argument (default: "hi")',
        "choices": UNDEFINED,
    }
    assert conpyguration.get("init_arguments").get("literal_arg") == {
        "value_type": Literal,
        "default": 3,
        "description": "A description of the argument (default: 3)",
        "choices": (3, "hi"),
    }
    assert list(conpyguration.get("methods").keys()) == ["foo"]
    assert conpyguration.get("methods").get("foo") == {
        "description": "A dummy method with annotations and docstrings",
        "module_name": "test_conpyguration",
        "function_name": "DummyClassWithAnnotationsAndDocstrings.foo",
        "arguments": {
            "bar": {
                "value_type": str,
                "default": UNDEFINED,
                "description": "A description of the argument",
                "choices": UNDEFINED,
            }
        },
        "return_spec": {"value_type": bool, "description": "A description of the return value"},
    }
