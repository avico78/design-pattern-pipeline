from typing import Dict, List, Set


# note that for multitask handling your tasks should all have (*args, **kwargs)
# signature, where args is the result of the previous tasks while kwargs are params

def remove_whitespace(data: List[List[str]], **kwargs):
    result = []
    for row in data:
        result.append([x.strip().strip("/n") for x in row])
    return result


def convert_to_dictionary(data: List, **kwargs):
    # here I pretend that data have no header and rename is other transformation
    # in reality it should be probably handled in read csv
    result = []
    for row in data:
        result.append({f"field_{index + 1}": value for index, value in enumerate(row)})
    return result


def rename_fields(data: List, **kwargs):
    field_map: Dict = kwargs.get("field_map")
    result = []
    for row in data:
        result.append({field_map.get(key, key): value for key, value in row.items()})
    return result


def uppercase(data: List, **kwargs):
    field_map: Set = kwargs.get("fields_to_apply")
    result = []
    for row in data:
        result.append(
            {key: value if key not in field_map else value.upper()
             for key, value in row.items()})
    return result
