def sum_of_elements(lst):
    if len(lst) == 0: #Перевірка, якщо масив порожній, то виводимо 0
        return 0
    sum_of_elements = sum(lst[i] for i in range(0, len(lst), 2)) #Знаходимо суму елементів із парними індексами за допомогою ф-ії range
    return sum_of_elements * lst[-1] #Домножаємо суму на останній елемент нашого масиву
lst1 = [0]
lst2 = [1, 2, 3, 4, 5, 6]
result1 = sum_of_elements(lst1)
result2 = sum_of_elements(lst2)
print(lst1, result1, sep=" -> ") #Виводимо результат для двох масивів
print(lst2, result2, sep=" -> ")