#!/usr/bin/python3
""" Function that adds a new attribute to an object if it is  possible to"""


def add_attribute(obj, a_name, a_value):
    """ Function to  add  an attribute to the class"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")

    setattr(obj, a_name, a_value)
