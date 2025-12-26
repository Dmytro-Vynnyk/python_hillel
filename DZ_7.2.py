def correct_sentence(text: str) -> str:
    text = text.capitalize()

    if not text.endswith('.'):
        text += '.'
        return text
    return text


print(correct_sentence("Greetings, friends."))
