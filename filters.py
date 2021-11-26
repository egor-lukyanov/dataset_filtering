import numbers


def prepare_filter(func):
    def wrapper(item: tuple):
        if item:
            key, value = item
            return func(key, value)
    return wrapper


@prepare_filter
def filter_odd(key, value) -> tuple:
    if isinstance(value, int) and value % 2 == 0:
        return key, value


@prepare_filter
def filter_number(key, value) -> tuple:
    if isinstance(value, numbers.Number):
        return key, value

@prepare_filter
def filter_alphakeys(key, value) -> tuple:
    if key.isalpha():
        return key.lower(), value


@prepare_filter
def filter_notempty(key, value) -> tuple:
    if value is not None:
        return key, value
