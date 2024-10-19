def correct_sentence(text):
    text = text.capitalize() #Робиму першу літеру в реченні великою
    if not text.endswith('.'): #Якщо речення не закінчується крапкою, то додаємо її
        text += '.'
    return text

assert correct_sentence("greetings, friends")
assert correct_sentence("hello")
assert correct_sentence("Greetings. Friends")
assert correct_sentence("Greetings, friends.")
assert correct_sentence("greetings, friends.")
print('ОК')
