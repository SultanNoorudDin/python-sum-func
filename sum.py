def my_sum(iterable, start=0):
    """
    Calculate the sum of all the items in an iterable.

    Parameters:
    iterable (iterable): An iterable containing numeric values to be summed.
    start (optional, numeric): An optional starting value for the sum.
                              Defaults to 0 if not provided.

    Returns:
    numeric: The sum of all the values in the iterable, starting from the
             provided 'start' value.

    Examples:
    >>> my_sum([1, 2, 3, 4, 5])
    15

    >>> my_sum([1.5, 2.5, 3.5], start=10)
    18.5

    >>> my_sum(range(1, 101))
    5050
    """
    result = start
    for item in iterable:
        result += item
    return result

# Usage examples:
result1 = my_sum([1, 2, 3, 4, 5])
result2 = my_sum([1.5, 2.5, 3.5], start=10)
result3 = my_sum(range(1, 101))

print(result1)  # Output: 15
print(result2)  # Output: 18.5
print(result3)  # Output: 5050
