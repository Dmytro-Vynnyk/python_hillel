def second_index(text: str, some_str: str) -> int | None:
    """
    Returns the index of the second occurrence of `some_str` in `text`.

    If `some_str` does not occur at least twice in `text`, returns None.

    :param text: The text where the search is performed.
    :param some_str: The substring to find (can contain multiple characters).
    :return: Index of the second occurrence, or None if it doesn't exist.
    """
    first_index = text.find(some_str)

    if first_index == -1:
        return None

    second_index_value = text.find(some_str, first_index + len(some_str))

    return None if second_index_value == -1 else second_index_value
