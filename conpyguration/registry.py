import functools
import inspect
from typing import Any

from conpyguration.conpy import get_function_conpyguration
from conpyguration.storage import Storage
from conpyguration.types import UNDEFINED, FunctionCallSpec, FunctionSpec
from conpyguration.utils import get_datetime_now

function_tracker_storage = Storage[FunctionCallSpec]()


def wrap_function_tracker(key: str, func: Any) -> Any:
    """wrap a function to track the conpyguration

    Args:
        key (str): The key to store the conpyguration under
        func (Any): The function to wrap

    Returns:
        wrapped_func (Any): The wrapped function
    """
    if not inspect.isfunction(func):
        raise TypeError("The input should be a function")

    func_spec: FunctionSpec = get_function_conpyguration(func)
    function_tracker_storage.add_item(key, FunctionCallSpec())

    @functools.wraps(func)
    def inner(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        bound.apply_defaults()
        function_tracker_storage.get_item(key).update(
            FunctionCallSpec(
                module_name=func_spec.get("module_name"),
                function_name=func_spec.get("function_name"),
                arguments=bound.arguments,
                called_at=get_datetime_now(),
            )
        )
        return func(*args, **kwargs)

    return inner


def get_function_tracker(key: str) -> FunctionCallSpec:
    """Get the conpyguration of a function or class

    Args:
        key (str): The key to get the conpyguration of

    Returns:
        FunctionCallSpec: The conpyguration of the function
    """
    return function_tracker_storage.get_item(key)
