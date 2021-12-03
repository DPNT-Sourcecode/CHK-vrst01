

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not isinstance(friend_name, str):
        raise TypeError("A string was not provided as friend name.")
    return "".join(["Hello ", friend_name])
