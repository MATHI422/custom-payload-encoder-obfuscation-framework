def reverse_text(text):
    return text[::-1]


def split_text(text):
    return " + ".join(list(text))


def add_separator(text, separator="#"):
    return separator.join(text)


def remove_separator(text, separator="#"):
    return text.replace(separator, "")


def escape_text(text):
    return ''.join(f'\\x{ord(c):02x}' for c in text)


def unescape_text(text):
    return bytes.fromhex(text.replace("\\x", "")).decode()
