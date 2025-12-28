def is_palindrome(text: str) -> bool:
    """
    Checks whether the given text is a palindrome.

    The check ignores punctuation, spaces and letter case.

    :param text: Input string to check
    :return: True if the text is a palindrome, False otherwise
    """
    filtered = filter(str.isalnum, text)
    lowered = map(str.lower, filtered)
    cleaned_text = "".join(lowered)
    return cleaned_text == cleaned_text[::-1]


print(is_palindrome('A man, a plan, a canal: Panama'))
