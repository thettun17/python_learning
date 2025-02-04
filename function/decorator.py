# modify a function's behavior without altering its original code
def greet(name):
    return f"Hello {name}"


def uppercase_decorator(function):
    def wrapper(name):
        result = function(name)
        return result.upper()

    return wrapper


uppercase_greet = uppercase_decorator(greet)
print(uppercase_greet("Thet Tun"))


# Decorator With @ sign
def lower_decorator(function):
    def wrapper(name):
        result = function(name)
        return result.lower()

    return wrapper


@lower_decorator
def lower_greet(name):
    return f"Hello {name}"


print(lower_greet("Thet Tun"))
