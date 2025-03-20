# ConPYguration
Configure your Python function or class with ConPYguration. ConPYguration is a Python library that allows you to easily configure your Python functions or classes with a configuration file or `Dictionary`.

## Installation
```bash
pip install conpyguration
```

## Usage
### Basic Function
```python
from conpyguration import get_conpyguration

def my_function(a, b=1) -> int:
    return a + b

get_conpyguration(my_function)
# {
#     'description': <class 'conpyguration.types.UNDEFINED'>,
#     'module_name': '__main__',
#     'function_name': 'my_function',
#     'arguments': {
#         'a': {
#             'value_type': <class 'conpyguration.types.UNDEFINED'>,
#             'default': <class 'conpyguration.types.UNDEFINED'>,
#             'description': <class 'conpyguration.types.UNDEFINED'>,
#             'choices': <class 'conpyguration.types.UNDEFINED'>
#         },
#         'b': {
#             'value_type': <class 'conpyguration.types.UNDEFINED'>,
#             'default': 1,
#             'description': <class 'conpyguration.types.UNDEFINED'>,
#             'choices': <class 'conpyguration.types.UNDEFINED'>
#         },
#     },
#     'return_spec': {
#         'value_type': <class 'int'>,
#         'description': <class 'conpyguration.types.UNDEFINED'>
#     }
# }
```

### Functions with docstrings
```python
def my_function(a: int, b: int=1) -> int:
    """
    This is a function that adds two numbers together.

    Args:
        a (int): The first number.
        b (int, optional): The second number. Defaults to 1.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

get_conpyguration(my_function)
# {
#     'description': 'This is a function that adds two numbers together.',
#     'module_name': '__main__',
#     'function_name': 'my_function',
#     'arguments': {
#         'a': {
#             'value_type': <class 'int'>,
#             'default': <class 'conpyguration.types.UNDEFINED'>,
#             'description': 'The first number.',
#             'choices': <class 'conpyguration.types.UNDEFINED'>
#         },
#         'b': {
#             'value_type': <class 'int'>,
#             'default': 1,
#             'description': 'The second number. Defaults to 1.',
#             'choices': <class 'conpyguration.types.UNDEFINED'>
#         }
#     },
#     'return_spec': {
#         'value_type': <class 'int'>,
#         'description': 'The sum of the two numbers.'
#     }
# }
```

### Functions with Union types
```python
from typing import Union

def my_function(a: Union[int, float]):
    return

get_conpyguration(my_function)
# {
#     'description': <class 'conpyguration.types.UNDEFINED'>,
#     'module_name': '__main__',
#     'function_name': 'my_function',
#     'arguments': {
#         'a': {
#             'value_type': (<class 'int'>, <class 'float'>),
#             'default': <class 'conpyguration.types.UNDEFINED'>,
#             'description': <class 'conpyguration.types.UNDEFINED'>,
#             'choices': <class 'conpyguration.types.UNDEFINED'>
#         }
#     },
#     'return_spec': <class 'conpyguration.types.UNDEFINED'>
# }
```

### Functions with Literal types (choice)
```python
from typing import Literal

def my_function(a: Literal[1, 2, 3]):
    return

get_conpyguration(my_function)
# {
#     'description': <class 'conpyguration.types.UNDEFINED'>,
#     'module_name': '__main__',
#     'function_name': 'my_function',
#     'arguments': {
#         'a': {
#             'value_type': typing.Literal,
#             'default': <class 'conpyguration.types.UNDEFINED'>,
#             'description': <class 'conpyguration.types.UNDEFINED'>,
#             'choices': (1, 2, 3)
#         }
#     },
#     'return_spec': <class 'conpyguration.types.UNDEFINED'>
# }
```

### Class
Coming soon...
