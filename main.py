user_input = int(input("Введіть 4-х значне число: ")) #Просимо користувача ввести 4-х значне число і робимо його цілим
number1 = user_input // 1000 #Отримуємо першу цифру
number2 = (user_input % 1000) // 100 #Друга цифра
number3 = (user_input % 100) // 10 #Третя цифра
number4 = user_input % 10 #Четверта цифра
print(number1) #Друкуємо цифри в стовпчик
print(number2)
print(number3)
print(number4)