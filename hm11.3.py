def is_even(number: int) -> bool:
    my_list = [0, 1, 3, 5, 7, 9]
    if number in my_list or int(str(number)[-1]) in my_list:
        return False
    else:
        return True

print(is_even(2494563894038**2)) # == True, 'Test1'
print(is_even(1056897**2)) # == False, 'Test2'
print(is_even(24945638940387**3)) # == False, 'Test3'
