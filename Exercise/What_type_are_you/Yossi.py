# exit(0)
# create a function that recieves an external argument and decides what to do accordint to the type,
# if its a string, return  True if the string is longer than 5
# if its an int return its power of 3
# if its a flot then return its division by 5.
# if its a list return the amount of list items
# if its a dict PRINT the dict items in seperate lines


def number_of_items(lst):
    items_number = 0
    for item in lst:
        items_number += 1
    return items_number


def string_length(string):
    chars_count = 0
    for item in string:
        chars_count += 1
    return chars_count


def who_and_what(param):
    if type(param) is str:
        if number_of_items(param) > 5:
            return True
        else:
            return False
    elif type(param) == int:
        return param ** 3
    elif type(param) == float:
        return param / 5
    elif type(param) == list:
        return number_of_items(param)
    elif type(param) == dict:
        for k, v in param.items():
            print(k, v, sep="  :  ")


if __name__ == "__main__":
    short_str = 'elik'
    long_str = 'elik zakai'
    int_val = 5
    float_val = 6.5
    list_val = [4, 5, 3, 'h', 'u', 'g', 'e']
    dict_val = {'name': 'elik', 'age': 45, 'annoying': 'never', 'nice': 'sometimes', 'funny': 'always'}
    #
    # who_and_what(dict_val)
    #
    # print(who_and_what(short_str))
    # print(who_and_what(long_str))
    # print(who_and_what(int_val))
    # print(who_and_what(float_val))
    # print(who_and_what(list_val))

who_and_what(dict_val)
assert not who_and_what(short_str)
assert who_and_what(long_str)
assert who_and_what(int_val) == 125
assert who_and_what(float_val) == 1.3
assert who_and_what(list_val) == 7


# this should be the output:
# name  :  elik
# age  :  45
# annoying  :  always
# nice  :  sometimes
# funny  :  never
# False
# True
# 125
# 1.3
# 7
