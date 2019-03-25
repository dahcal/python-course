import os
import json

with open("file_definitions.json") as data_file:
    data = json.loads(data_file.read())

class Info:
    """
    Generates object with given arguments
    Takes:
        type_ (list) -> list of file types
        extension (list) -> list of file extensions
    Returns:
        (<class 'file_info.Info'>) -> Class instance
    """

    def __init__(self, type_, extension):
        self.type = type_
        self.extension = extension

    def type_matches(self, type_):
        """ Checks if file type matches with given type """
        return type_ in self.type

    def extension_matches(self, extension):
        """ Checks if file extension matches with given extension """
        return extension in self.extension


def get(obj):
    """
    Determines file format and picks suitable file types and extensions types
    Takes:
        obj (bytes) -> byte sequence (128 bytes are enough) can i do it wil 16 for this assignment?
    Returns:
        (<class 'file_info.Info'>) -> Class instance
    """

    if not isinstance(obj, bytes):
        raise TypeError("Object type must be bytes")

    info = {
        "type": dict(),
        "extension": dict(),
    }

    stream = " ".join(['{:02X}'.format(byte) for byte in obj])

    for element in data:
        for signature in element["signature"]:
            offset = element["offset"] * 2 + element["offset"]
            if signature == stream[offset:len(signature) + offset]:
                for key in ["type", "extension"]:
                    info[key][element[key]] = len(signature)

    for key in ["type", "extension"]:
        info[key] = [element for element in sorted(info[key], key=info[key].get, reverse=True)]

    return Info(info["type"], info["extension"])

def supported_types():
    """ Returns a list of supported file types """
    return sorted(set([x["type"] for x in data]))


def supported_extensions():
    """ Returns a list of supported file extensions """
    return sorted(set([x["extension"] for x in data]))