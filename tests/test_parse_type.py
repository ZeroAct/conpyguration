from typing import Literal, Union

import pytest

from conpy.conpy import parse_type


def test_plain_type():
    assert parse_type(str) is str


def test_union_plain_types():
    result = parse_type(Union[str, int])
    assert isinstance(result, tuple)
    assert result == (str, int)


def test_literal():
    result = parse_type(Literal[3, "hi"])
    assert result is Literal


def test_union_plain_and_literal():
    with pytest.raises(TypeError):
        parse_type(Union[str, Literal[3]])
