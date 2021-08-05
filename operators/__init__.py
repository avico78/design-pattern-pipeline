from exceptions import UnknownOperator
from .loads import read_csv
from .transformations import (
    remove_whitespace,
    uppercase,
    rename_fields,
    convert_to_dictionary
)

operators = {
    "read_csv": read_csv,
    "remove_whitespace": remove_whitespace,
    "uppercase": uppercase,
    "rename_fields": rename_fields,
    "convert_to_dictionary": convert_to_dictionary,
}


def none_operator(*args, **kwargs):
    # this should probably be handled in tasks init to fail quick not at runtime
    raise UnknownOperator("Unknown operator passed!")
