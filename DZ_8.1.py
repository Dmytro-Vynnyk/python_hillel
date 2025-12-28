def add_one(some_list):
    """
    Adds one to the number represented by a list of digits
    and returns the result as a list of digits.

    :param some_list: List of digits representing a number
    :return: List of digits after adding one
    """
    number = int("".join(map(str, some_list)))
    number += 1
    return list(map(int, str(number)))


print(add_one([1, 2, 3, 4]))
