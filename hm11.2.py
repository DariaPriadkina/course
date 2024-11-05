def number_in_cube(number):
    number **= 3
    return number

def generate_cube_numbers(end):
    for number in range(2, end):
        cube = number_in_cube(number)
        if cube <= end:
            yield cube
        else: return


from inspect import isgenerator

gen = generate_cube_numbers(1)
print(isgenerator(gen)) # == True, 'Test0'
print(list(generate_cube_numbers(10))) # == [8], 'оскільки воно менше 10.'
print(list(generate_cube_numbers(100))) # == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
print(list(generate_cube_numbers(1000))) # == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
