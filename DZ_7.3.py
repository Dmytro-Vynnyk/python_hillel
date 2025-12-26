def second_index(text: str, some_str: str) -> int:
    first_index = text.find(some_str)

    if first_index == -1:
        return None

    second_index = text.find(some_str, first_index + len(some_str))

    return None if second_index == -1 else second_index

print(second_index("hihih", "h"))
