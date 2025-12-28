def find_unique_value(some_list: list) -> list | None:
    """
    Finds and returns the unique value in a list.

    A unique value is a value that appears exactly once in the list.

    :param some_list: List of numbers
    :return: Unique number
    """
    for item in set(some_list):
        if some_list.count(item) == 1:
            return item


print(find_unique_value([5, 5, 5, 2, 2, 0.5]))
