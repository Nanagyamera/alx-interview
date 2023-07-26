#!/usr/bin/python3
"""
Main file for testing
"""

def validUTF8(data):
    def get_num_bytes_for_utf8(char):
        if char & 0x80 == 0x00:  # 1-byte character (0xxxxxxx)
            return 1
        elif char & 0xE0 == 0xC0:  # 2-byte character (110xxxxx)
            return 2
        elif char & 0xF0 == 0xE0:  # 3-byte character (1110xxxx)
            return 3
        elif char & 0xF8 == 0xF0:  # 4-byte character (11110xxx)
            return 4
        else:
            return -1  # Invalid UTF-8 character

    i = 0
    while i < len(data):
        num_bytes = get_num_bytes_for_utf8(data[i])
        if num_bytes == -1:  # Invalid character
            return False

        # Check if there are enough bytes left for the current character
        if i + num_bytes > len(data):
            return False

        # Check if the following bytes are of the form 10xxxxxx
        for j in range(i + 1, i + num_bytes):
            if data[j] & 0xC0 != 0x80:
                return False

        i += num_bytes

    return True
