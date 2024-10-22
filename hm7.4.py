def common_elements():
    #створюємо два списки з числами. перший - кратний 3, другий - п'яти
    list_of_three = [x for x in range(100) if x % 3 == 0]
    list_of_five = [x for x in range(100) if x % 5 == 0]
    #перетворюємо ці списки на множини
    set_of_three = set(list_of_three)
    set_of_five = set(list_of_five)
    #знаходимо перетин
    intersection_set = set_of_three.intersection(set_of_five)
    return intersection_set

print(common_elements())
