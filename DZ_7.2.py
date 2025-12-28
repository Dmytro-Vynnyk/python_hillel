def correct_sentence(text: str) -> str:
    """
    Corrects a sentence so that it starts with a capital letter
    and ends with a period.

    If the sentence already ends with a period, no extra one is added.

    :param text: Input sentence as a string
    :return: Corrected sentence
    """
    text = text.capitalize()

    if not text.endswith('.'):
        text += '.'
        return text
    return text


print(correct_sentence("Greetings, friends."))
