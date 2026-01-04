def popular_words(text: str, words: list[str]) -> dict[str, int]:
    """
    Counts how many times each word from the given list appears in the text.

    The search is case-insensitive. If a word does not appear in the text,
    it is included in the result with value 0.

    :param text: Input text in which words are searched
    :param words: List of words to count (in lowercase)
    :return: Dictionary with words as keys and their occurrence counts as values
    """
    text_words = text.lower().split()
    return {word: text_words.count(word) for word in words}


print(popular_words("When I was One I had just begun When I was Two I was nearly new", ["i", "was", "three", "near"]))
