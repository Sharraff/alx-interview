#!/usr/bin/python3
"""
check for unicode
"""


def validUTF8(data):
    """
    validUTF8: checks for utf8 encoding
    return: boolean
    """
    leader_count = 0
    for byte in data:
        byte = byte & 0xFF

        if leader_count == 0:
            if byte >> 7 == 0b0:
                leader_count = 0
            elif byte >> 5 == 0b110:
                leader_count = 1
            elif byte >> 4 == 0b1110:
                leader_count = 2
            elif byte >> 3 == 0b11110:
                leader_count = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                leader_count -= 1
            else:
                return False
        return leader_count == 0
