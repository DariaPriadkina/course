def find_unique_value(some_list):
    number = None
    for unique_number in some_list:
        if some_list.count(unique_number) == 1:
            number = unique_number
            break
    return number

print(find_unique_value([1, 2, 1, 1]))
print(find_unique_value([2, 3, 3, 3, 5, 5]))
print(find_unique_value([5, 5, 5, 2, 2, 0.5]))