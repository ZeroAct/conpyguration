import inspect
from typing import Any, Literal, Union, get_args, get_origin

import docstring_parser

from conpyguration.types import (
    UNDEFINED,
    ArgumentSpec,
    ClassSpec,
    FunctionSpec,
    ReturnSpec,
)


def parse_type(value_type: type) -> Union[type, tuple, list]:
    """Parse type to conpy type

    Args:
        value_type (type): The type to parse. Can be a python type.

    Raises:
        TypeError: If the type is not supported.

    Returns:
        Union[type, list[type], tuple[type, list[Any]]]: The parsed type.

    Example:
        >>> parse_type(str)
        <class 'str'>
        >>> parse_type(Union[str, int])
        (<class 'str'>, <class 'int'>)
        >>> parse_type(Literal[3, "hi"])
        Literal
        >>> parse_type(Union[str, Literal[3]])

    """
    origin = get_origin(value_type)

    if origin is None:
        return value_type

    if origin is Literal:
        return Literal

    if origin is Union:
        args = get_args(value_type)
        for arg in args:
            if get_origin(arg) is Literal:
                raise TypeError("Union with Literal is not supported")
        return args

    return value_type


def get_conpyguration(func: Any, docstring: str = None) -> FunctionSpec:
    """Get the conpyguration of a function or class

    Args:
        func (Any): The function or class to get the conpyguration of
        docstring (str): The docstring of the function or class

    Returns:
        FunctionSpec: The conpyguration of the function or class
    """
    if not inspect.isfunction(func):
        raise TypeError("The input should be a function or a class")

    signature = inspect.signature(func)
    docstring = docstring or func.__doc__ or UNDEFINED
    docstring_parse = docstring_parser.parse(docstring) if docstring != UNDEFINED else UNDEFINED

    docstring_short_description = (
        docstring_parse.short_description if docstring_parse != UNDEFINED else UNDEFINED
    )

    docstring_arg_dict = (
        {p.arg_name: p.description for p in docstring_parse.params}
        if docstring_parse != UNDEFINED
        else UNDEFINED
    )
    docstring_return = docstring_parse.returns if docstring_parse != UNDEFINED else UNDEFINED

    arguments = {}
    for name, parameter in signature.parameters.items():
        value_type = (
            parse_type(parameter.annotation)
            if parameter.annotation != inspect.Parameter.empty
            else UNDEFINED
        )
        default = parameter.default if parameter.default != inspect.Parameter.empty else UNDEFINED
        description = docstring_arg_dict.get(name) if docstring_arg_dict != UNDEFINED else UNDEFINED
        choices = get_args(parameter.annotation) if value_type == Literal else UNDEFINED

        argument = ArgumentSpec(
            value_type=value_type, default=default, description=description, choices=choices
        )
        arguments[name] = argument

    return_spec = (
        ReturnSpec(
            value_type=parse_type(signature.return_annotation)
            if signature.return_annotation != inspect.Parameter.empty
            else UNDEFINED,
            description=docstring_return.description if docstring_return != UNDEFINED else UNDEFINED,
        )
        if signature.return_annotation != inspect.Parameter.empty
        else UNDEFINED
    )

    return FunctionSpec(
        description=docstring_short_description,
        module_name=func.__module__ if hasattr(func, "__module__") else UNDEFINED,
        function_name=func.__name__ if hasattr(func, "__name__") else UNDEFINED,
        arguments=arguments,
        return_spec=return_spec,
    )


def get_class_conpyguration(cls: Any, docstring: str = None) -> ClassSpec:
    """Get the conpyguration of a class

    Args:
        cls (Any): The class to get the conpyguration of
        docstring (str): The docstring of the class

    Returns:
        ClassSpec: The conpyguration of the class
    """
    if not inspect.isclass(cls):
        raise TypeError("The input should be a class")

    module_name = cls.__module__ if hasattr(cls, "__module__") else UNDEFINED
    class_name = cls.__name__ if hasattr(cls, "__name__") else UNDEFINED

    docstring = docstring or cls.__doc__ or cls.__init__.__doc__ or UNDEFINED

    init_arguments = get_conpyguration(cls.__init__, docstring)
    init_arguments["arguments"].pop("self", None)

    methods = {}
    for name, method in cls.__dict__.items():
        if name.startswith("__"):
            continue

        if inspect.isfunction(method):
            config = get_conpyguration(method)
            config["arguments"].pop("self", None)
            config["function_name"] = class_name + "." + name
            methods[name] = config

    return ClassSpec(
        description=init_arguments["description"],
        module_name=module_name,
        class_name=class_name,
        init_arguments=init_arguments["arguments"],
        methods=methods,
    )
