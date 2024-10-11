import random
first_list = []
#Створюємо список чисел із випадковою кількістю елементів від 3 до 10, з випадковими значеннями від 1 до 10
for i in range(random.randint(3, 10)):
    first_list.append(random.randint(1, 10))
print("Початковий список:", first_list)

#Формуємо новий список
new_list = [first_list[0]] #Додаємо в новий список перший елемент з індексом 0
new_list.append(first_list[2]) #Потім отримуємо третій елемент у новий список з індексом 2
new_list.append(first_list[-2]) #Отримуємо другий елемент з кінця
print("Новий список: ", new_list) #Виводимо результат