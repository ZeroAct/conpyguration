from typing import Any, TypedDict, Union


class UNDEFINED:
    """A class to represent an undefined value"""

    def __repr__(self) -> str:
        return "Undefined"


class ArgumentSpec(TypedDict):
    """A class to represent the specification of a function argument

    Attributes:
        value_type (type | tuple[type]): The type of the argument. If the argument can be of multiple types, this should be a tuple of types.
        default (Any): The default value of the argument.
        description (str): A description of the argument.
        choices (tuple[Any]): A tuple of possible values for the argument. This field is for Literal types.
    """

    value_type: Union[type, tuple[type]]
    default: Any
    description: str
    choices: tuple[Any]


class ReturnSpec(TypedDict):
    """A class to represent the specification of a function return value

    Attributes:
        value_type (type | tuple[type]): The type of the return value. If the return value can be of multiple types, this should be a tuple of types.
        description (str): A description of the return value.
    """

    value_type: Union[type, tuple[type]]
    description: str


class FunctionSpec(TypedDict):
    """A class to represent the specification of a function

    Attributes:
        name (str): The name of the function.
        description (str): A description of the function.
        module_name (str): The name of the module containing the function.
        arguments (dict[str, ArgumentSpec | list[dict[str, ArgumentSpec]] | list[ArgumentSpec]]): A dictionary mapping argument names to their specifications.
        return_type (ReturnSpec): The specification of the return value of the function.
    """

    description: str
    module_name: str
    function_name: str
    arguments: dict[str, ArgumentSpec]
    return_spec: ReturnSpec
