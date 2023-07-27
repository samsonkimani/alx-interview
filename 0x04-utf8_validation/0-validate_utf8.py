#!/usr/bin/python3

"""
a function that determines if the given dataset represents a valid utf8
encoding

Args:
    data: an array of data
"""


def validUTF8(data):
    """ valid utf-8"""

    def following_byte(num):
        return (num >> 6) == 0b10

    bytes_needed = 0

    for num in data:
        if bytes_needed == 0:
            if (num >> 7) == 0b0:
                continue
            elif (num >> 5) == 0b110:
                bytes_needed = 1
            elif (num >> 4) == 0b1110:
                bytes_needed = 2
            elif (num >> 3) == 0b11110:
                bytes_needed = 3
            else:
                return False
        else:
            if not following_byte(num):
                return False
            bytes_needed -= 1
    if bytes_needed > 0:
        return False

    return True
