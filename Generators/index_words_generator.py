def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ': # we are assuming that words are seperated by single space
            yield index + 1

indexes_of_words = list(index_words_iter("Hello hii"))
print(indexes_of_words)