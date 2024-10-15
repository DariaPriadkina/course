number = int(input("Введіть ціле число: "))
#За допомогою цикла перемножуємо цифри введеного числа поки воно більше 9
while number > 9:
    result = 1 #Створюємо змінну для результату
    for digit in str(number): #Перетворюємо число в рядок для ітерації по цифрах
        result *= int(digit) #Перемножуємо
    number = result
print("Результат:", number)