import string
import keyword

test_name = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value',
             'Get_value', 'get_Value', 'getValue', '3m', 'm3', 'assert', 'assert_exception']
for test_variable in test_name:
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist: #Зарезервовані слова
            print(f"Error. Found {test_variable} is keyword.")

        elif test_variable == '_': #Для одного підкреслення
            print(f"{test_variable} is a correct name.")

        elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.count(" ") == 0:
            is_correct = True
            for symbol in string.punctuation.replace("_", ""): #Символи окрім "_"
                if symbol in test_variable:
                    is_correct = False
                    print(f"Error. Found {test_variable} in variable name.")
                    break

            first_underscore_index = test_variable.find("_")
            if first_underscore_index != -1: #Для подвійних підкреслень
                second_underscore_index = test_variable.find("_", first_underscore_index + 1)
                if second_underscore_index != -1 and second_underscore_index - first_underscore_index == 1:
                    is_correct = False
                    print(f"Error. Found double '_' in variable name.")
            if is_correct:
                print(f"{test_variable} is correct name.")
        else:
            print(f"Error. Found {test_variable} in variable name.")
    else:
        print("Incorrect variable length.")