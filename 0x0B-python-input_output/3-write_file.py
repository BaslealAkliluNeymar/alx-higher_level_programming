#!/usr/bin/python3
"""3-write_file.
Writes in a text file.
"""


def write_file(filename="", text=""):
    """Writing text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)
