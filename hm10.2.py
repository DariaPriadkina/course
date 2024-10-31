import string

def first_word(text):
    text = text.lstrip(string.punctuation).replace(',', ' ').replace('.', ' ').split()
    return text[0]


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))