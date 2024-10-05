def split_list(lst):
    if len(lst) == 0: #Якщо список порожній, то повертаэмо два порожны списки
        return [[], []]
    else:
        mid = (len(lst) + 1) // 2 #Знаходимо середину списку
        first_half = lst[:mid] #Перша частина
        second_half = lst[mid:] #Друга частина
        return [first_half, second_half] #У результаті повертаємо список із двох списків

lst1 = [1,2,3,4,5] #Для непарної кількості елеменетів у списку
lst2 = [0,9,8,7] #Для парної кількості
lst3 = [] #Для порожнього списку

#Виводимо результат
print(split_list(lst1))
print(split_list(lst2))
print(split_list(lst3))