# exit(0)
# create a function that recieves an external argument and decides what to do accordint to the type,
# if its a string, return  True if the string is longer than 5
# if its an int return its power of 3
# if its a flot then return its division by 5.
# if its a list return the amount of list items
# if its a dict PRINT the dict items in seperate lines


from functools import reduce

short_str = 'elik'
long_str = 'elik zakai'
int_val = 5
float_val = 6.5
list_val = [4, 5, 3, 'h', 'u', 'g', 'e']
dict_val = {'name': 'elik', 'age': 45, 'annoying': 'always', 'nice': 'sometimes', 'funny': 'never'}

def notasomething(obj, cls): return ('not ' if not isinstance(obj, cls) else 'its a ') + cls.__name__
def dictation(x): return notasomething(x, dict)
def stringy(x):   return notasomething(x, str)
def lister(x):    return notasomething(x, list)
def floater(x):   return notasomething(x, float)

def who_and_what(something):
    def lon(abc): return reduce(lambda x, y: x + y, [1 for x in abc])
    match type(something):
        case x if x is str:   return lon(something) > 5
        case x if x is int:   return something ** 3
        case x if x is float: return something / 5
        case x if x is list:  return lon(something)
        case x if x is dict:  return '\n'.join([f'{k}: {v}' for k, v in something.items()])


print(who_and_what(short_str))
print(who_and_what(long_str))
print(who_and_what(int_val))
print(who_and_what(float_val))
print(who_and_what(list_val))

print(dictation(long_str))
print(stringy(long_str))
print(lister(long_str))
print(floater(long_str))
print(dictation(long_str))



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
