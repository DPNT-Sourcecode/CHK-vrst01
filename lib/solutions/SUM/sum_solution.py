# noinspection PyShadowingBuiltins,PyUnusedLocal
class InputTypeError(Exception):
    """Error to raise when one of the inputs is not of the correct type/"""
    pass


class InputRangeError(Exception):
    """Error to raise when one of the inputs is not within the correct range."""
    pass


def compute(x, y):
    """Compute and return sum of integer inputs within range(0-100)"""
    if not (isinstance(x, int) and isinstance(y, int)):
        raise InputTypeError("A value provided is not an integer")
    # TODO: The instructions for this task are ambiguous as they do not state which, if any, of the aspects
    # of the range are inclusive or exclusive; "between" is ambiguous, defaulting to python range functionality
    # which is inclusive of lower bound and exclusive of higher
    if x not in range(0,100):
        raise InputRangeError("The input {} is not in range(0-100).".format(x))
    if y not in range(0,100):
        raise InputRangeError("The input {} is not in range(0-100).".format(y))
    return x+y

