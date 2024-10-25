def add_one(some_list):
    number = int(''.join([str(char) for char in some_list])) + 1
    some_list = list(int(char) for char in str(number))
    return some_list


print(add_one([1, 2, 3, 4]))
print(add_one([9, 9, 9]))
print(add_one([0]))
print(add_one([9]))