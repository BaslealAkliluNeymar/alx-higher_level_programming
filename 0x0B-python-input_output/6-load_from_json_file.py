#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ Function that creates an Object from JSON  """
    with open(filename, 'r') as f:
        return (json.load(f))
 
