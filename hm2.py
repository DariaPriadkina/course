user_input = int(input("Введіть 5-ти значне число: ")) #Просимо користувача ввести 5-ти значне число та перетворюємо його в ціле
n1 = user_input % 10 #Отримуємо останню цифру
n2 = (user_input // 10) % 10 #Другу з кінця
n3 = (user_input // 100) % 10 #Третю
n4 = (user_input // 1000) % 10 #Четверту
n5 = (user_input // 10000) % 10 #П'яту
reversed_number = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5 #Формуємо перевернуте число
print("Перевернути число: ", reversed_number) #Виводимо отримане число