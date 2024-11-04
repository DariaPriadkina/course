def prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_generator(end):
    number = 2
    while number <= end:
        if prime(number) is True:
            yield number
        number += 1

from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen)) # == True, 'Test0'
print(list(prime_generator(10))) # == [2, 3, 5, 7], 'Test1'
print(list(prime_generator(15))) # == [2, 3, 5, 7, 11, 13], 'Test2'
print(list(prime_generator(29))) # == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'