def popular_words (text, words):
    text = text.lower().split()
    word_counter = {}
    for word in words:
        word_counter.setdefault(word, text.count(word))
    return word_counter

print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))