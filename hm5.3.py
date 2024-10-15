import string

user_input = input("Введіть рядок: ")
#Видаляємо знаки пунктуації та пробіли з рядка який ввів користувач
clean_string = ''.join(char for char in user_input if char not in string.punctuation)
#Розділяємо рядок на окремі слова
words = clean_string.split()

hashtag = '#'
#Додаємо до хештегу кожне слово з великої літери
for word in words:
    hashtag += word.title()
#Перевіряємо довжину рядка та якщо він більший за 140 символів - обмежуємо його до 140
if len(hashtag) > 140:
    hashtag = hashtag[:140]
#Виводимо результат
print(hashtag)