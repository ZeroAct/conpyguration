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
        description (str): A description of the function.
        module_name (str): The name of the module containing the function.
        function_name (str): The name of the function.
        arguments (dict[str, ArgumentSpec | list[dict[str, ArgumentSpec]] | list[ArgumentSpec]]): A dictionary mapping argument names to their specifications.
        return_type (ReturnSpec): The specification of the return value of the function.
    """

    description: str
    module_name: str
    function_name: str
    arguments: dict[str, ArgumentSpec]
    return_spec: ReturnSpec


class ClassSpec(TypedDict):
    """A class to represent the specification of a class

    Attributes:
        description (str): A description of the class.
        module_name (str): The name of the module containing the class.
        class_name (str): The name of the class.
        init_arguments (dict[str, ArgumentSpec]): A dictionary mapping argument names to their specifications
        methods (dict[str, FunctionSpec]): A dictionary mapping method names to their specifications.
    """

    description: str
    module_name: str
    class_name: str
    init_arguments: dict[str, ArgumentSpec]
    methods: dict[str, FunctionSpec]


class FunctionCallSpec(TypedDict):
    """A class to represent the specification of a function call

    Attributes:
        module_name (str): The name of the module containing the function.
        function_name (str): The name of the function.
        arguments (dict[str, Any]): A dictionary mapping argument names to their values.
        called_at (str): The time the function was called.
    """

    module_name: str
    function_name: str
    arguments: dict[str, Any]
    called_at: str
