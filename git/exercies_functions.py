# coding: utf-8


"""Python function used in the git Exercices.

This function are neither the best performing ones (in term of complexity and
Python performance) nor the most pythonic (min is already a function for
instance).
"""


def hello_world():
    """Print Hello world!."""
    print("Hello World!")


def ask_name():
    """Ask the name of the user."""
    print("Hello, what is your name?")
    name = input()
    print("Welcome to the git tutorial {}".format(name))


def factorial_iter(n: int):
    """Iteartively compute factorial of n."""
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


def factorial_rec_broken(n):
    """Non stopping recursive factorial function."""
    return n * factorial_rec_broken(n-1)


def factorial_rec(n):
    """Recursively compute the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n-1)


def simple_fibonacci(n):
    """Compute the nth Fibonacci number."""
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = a + b, a
    return a


def  my_min(t):
    """Compute the minimum of a non empty list."""
    current_min = t[0]
    for v in t:
        if current_min > v:
            current_min = v
    return current_min


def my_max(t):
    """Compute the maximum of a non empty list."""
    return - my_min([-v for v in t])


def vec_sum(a, b):
    """Compute the sum of two vector given in lists."""
    return [va + vb for va, vb in zip(a, b)]


def vec_dot(a, b):
    """Compute the dot product of two vectors given in lists."""
    return sum([va * vb for va, vb in zip(a, b)])
