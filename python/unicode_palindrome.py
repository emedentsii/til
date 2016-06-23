import unicodedata


def is_palindrome(s):
    if any(unicodedata.combining(c) for c in s):
        s = unicodedata.normalize('NFC', s)
    return s == s[::-1]