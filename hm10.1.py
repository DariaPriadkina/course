def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    while end > 0:
        yield begin
        begin = func(begin)
        end -= 1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
print(isgenerator(gen))
print(list(gen))