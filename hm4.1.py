def zeros_to_end_of_the_list(lst): #Цикл перевіряє кожне число списку чи є воно нулем і якщо так, то переміщує його в кінець списку
    for number in lst:
        if number == 0:
            lst.remove(number)
            lst.append(0)
    return lst
lst1 = [0]
lst2 = [1, 2, 3, 0, 4, 0, 5]
lst3 = [3, 99, 50, 0, 33, 0, 0, 88]
result1 = zeros_to_end_of_the_list(lst1)
result2 = zeros_to_end_of_the_list(lst2)
result3 = zeros_to_end_of_the_list(lst3)
print(result1)
print(result2)
print(result3)