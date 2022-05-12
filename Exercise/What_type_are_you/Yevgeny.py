# Create a function that recieves an external argument and decides
# what to do according to the type of the argument,
# if its a string, return  True if the string is longer than 5 and False if not
# if its an int return its power by 3
# if its a float then return its division by 5. /
# if its a list return the amount of list items
# if its a dict PRINT the dict items in seperate lines
#do not use len() method

def are_you_a_string(arg1):
    if type(arg1) == bool:
        print("it's a boolen")
    else:
        if isinstance(arg1,(int)):
            print("I'm a int")
            int(arg1)
            power3 = arg1 ** 3
            print("It's a number, in power of 3 the result is: ", power3)
            return False
        else:
            if isinstance(arg1,float):
                division = arg1 / 3
                print("It's a float, the division by 3 is: ",division)
            else:
                if type(arg1) is str:
                    print("it's a string")
                    counter = 0
                    for char in arg1:
                        counter += 1
                        if counter > 5:
                            print("bigger than 5 chars")
                            return True
                        else:
                            print("less than 5 chars, only ",counter, " chars in the string")
                            return False
                else:
                    if isinstance(arg1,(list)):
                        counter=0
                        for item in arg1:
                            counter+=1
                            print(counter)
                        print("it's a list with ", counter, " values")
                    else:
                        if isinstance(arg1, dict):
                            print("it's a dictionary, and the values inside are:")
                            for key in arg1:
                                print(key,":", arg1[key])
                        else:
                            print("unknown type")


#testing with diffrent types

arg1="Hello Elik"
are_you_a_string(arg1)
arg1="Hello"
are_you_a_string(arg1)
arg1=True
are_you_a_string(arg1)
arg1=4
are_you_a_string(arg1)
arg1=0.665
are_you_a_string(arg1)
arg1=[0,1,5,'a','b']
are_you_a_string(arg1)
arg1={"name":1, "age":5, "gander":"it's complicated"}
are_you_a_string(arg1)
