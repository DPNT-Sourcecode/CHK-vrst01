# noinspection PyShadowingBuiltins,PyUnusedLocal
class InputTypeError(Exception):
    """Error to raise when one of the inputs is not of the correct type/"""
    pass


class InputRangeError(Exception):
    """Error to raise when one of the inputs is not within the correct range."""
    pass

def _check_input_in_range(inputs):
    """Helper function to check inputs are within range and raise error if not."""
    for input in inputs:
        if input not in range(0,100):
            raise InputRangeError("The input {} is not in range(0-100).".format(input))

def compute(x, y):
    """Compute and return sum of integer inputs within range(0-100)."""
    if not (isinstance(x, int) and isinstance(y, int)):
        raise InputTypeError("A value provided is not an integer")
    # TODO: The instructions for this task are ambiguous as they do not state which, if any, of the aspects
    # of the range are inclusive or exclusive; "between" is ambiguous, defaulting to python range functionality
    # which is inclusive of lower bound and exclusive of higher
    # User helper function to minify code for checking if within range
    _check_input_in_range([x, y])
    return x+y
