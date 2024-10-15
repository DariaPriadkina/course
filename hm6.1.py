import string
user_input = input("Введіть через дефіс дві літери: ")

#Розділяємо введене на першу і другу літеру
letter1, letter2 = user_input.split('-')

#Використовуємо всі літери з string.ascii_letters
all_letters = string.ascii_letters

#Знаходимо індекси літер у рядку all_letters
start_index = all_letters.index(letter1)
end_index = all_letters.index(letter2)

#Формуємо результат включаючи останню введену літеру
result = all_letters[start_index:end_index + 1]
print("Символи між введеними літерами включно", result)