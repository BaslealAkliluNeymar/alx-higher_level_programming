#!/usr/bin/python3
"""10-class_to_json.
Returns the dictionary description with
simple data structure
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Creates a dict description of obj.
    Args:
        - obj: object to serialize
    Returns: dictionnary description of obj
    """

    return obj.__dict__
