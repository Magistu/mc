import re


def distinct(iterable, key):
    return dict((key(entry), entry) for entry in iterable).values()

def to_screaming_snake_case(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).upper()

def to_snake_case(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

def to_capitalized_text(snake_str):
    return " ".join(x.capitalize() for x in snake_str.lower().split("_"))

def to_pascal_case(snake_str):
    return "".join(x.capitalize() for x in snake_str.lower().split("_"))

def to_camel_case(snake_str):
    return snake_str[0].lower() + to_pascal_case(snake_str)[1:]