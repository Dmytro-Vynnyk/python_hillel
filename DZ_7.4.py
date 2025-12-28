def common_elements() -> set:
    """
    Generates two sets of numbers from 0 to 99:
    - the first set contains numbers divisible by 3
    - the second set contains numbers divisible by 5

    Returns a set of numbers that are present in both sets
    (their intersection).

    :return: A set of common elements divisible by both 3 and 5
    """
    multiples_of_3 = {i for i in range(100) if i % 3 == 0}
    multiples_of_5 = {i for i in range(100) if i % 5 == 0}

    return multiples_of_3 & multiples_of_5
