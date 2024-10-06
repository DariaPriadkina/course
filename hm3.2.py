#Список зі звичайними елементами
list = [1, 2, 3, 4, 5]
if len(list) > 1: #Перевіряємо чи у списку більше одного елемента
    last_element = list.pop() #Витягаємо останній елемент списку
    list.insert(0, last_element) #Вставляємо останній елемент на початок
print(list) #Виводимо результат

#Порожній список та список з одним елементом
empty_list = []
one_element_list = [1]

if len(empty_list) > 1:
    last_element = empty_list.pop()
    empty_list.insert(0, last_element)
print(empty_list)

if len(one_element_list) > 1:
    last_element = one_element_list.pop()
    one_element_list.insert(0, last_element)
print(one_element_list)