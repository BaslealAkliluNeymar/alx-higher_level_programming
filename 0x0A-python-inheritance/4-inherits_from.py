#!/usr/bin/python3
"""4-inherits_from.
Sees  if the given object is an instance of a class that inherited
 from the specified class.(directly or indirectly)"""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class that
    inherited from a_class.
    Args:
        - obj: object to look at
        - a_class: class to evaluate
    Returns: True or False
    """

    return isinstance(obj, a_class) and type(obj) != a_class
