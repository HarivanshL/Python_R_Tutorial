"""
    Data types:
    

    Data types are fundamental to learning programming. You have to know what kind of data you have 
    in order to know how to manipulate it.

    int - an integer
    float - a floating point number (a decimal)
    str - a string (multiple characters joined together; also can be thought of as a word; Ex: "Alice")
    bool - a boolean (either True or False)
    list - a list of items that you can change around
    tuple - a tuple is a list but it is not changeable
    dict - a dictionary that stores information in key value pairs
    set - unordered list that contains unique elements
    None - literally nothing. Represents absence of a value

    In python, theres no need to declare the variable type before assignment
    In some other languages youd have to write:
    int five = 5
    
    in python:
    five = 5

    if you want to change something you can also typecast something

    decimal_five = 5.0
    five = int(decimal_five)

    This will change five to hold the value 5







This may look daunting. Its just a function.
Functions take in arguments and return some sort of output

"""

"""
    Operators:

    Operators are special symbols in programming that perform operations on variables and values. 
    Python supports the following types of operators:

    Below are the common operators and their uses

    Reference this as an appendix if you want to figure out what to
    do when comparing data types

    1. Arithmetic Operators:
       +  : Addition
       -  : Subtraction
       *  : Multiplication
       /  : Division
       %  : Modulus
       ** : Exponentiation
       // : Floor Division

    2. Comparison Operators:
       == : Equal to
       != : Not equal to
       >  : Greater than
       <  : Less than
       >= : Greater than or equal to
       <= : Less than or equal to

    3. Logical Operators:
       and : Logical AND
       or  : Logical OR
       not : Logical NOT

    4. Assignment Operators:
       =  : Assign
       += : Add and assign
       -= : Subtract and assign
       *= : Multiply and assign
       /= : Divide and assign
       %= : Modulus and assign
       **= : Exponentiation and assign
       //= : Floor division and assign

    5. Bitwise Operators:
       &  : AND
       |  : OR
       ^  : XOR
       ~  : NOT
       << : Zero fill left shift
       >> : Signed right shift

    Example:
    a = 10
    b = 5

    # Arithmetic Operators
    sum = a + b  # 15
    difference = a - b  # 5
    product = a * b  # 50
    quotient = a / b  # 2.0
    modulus = a % b  # 0
    exponent = a ** b  # 100000
    floor_division = a // b  # 2

    # Comparison Operators
    is_equal = (a == b)  # False
    is_not_equal = (a != b)  # True
    is_greater = (a > b)  # True
    is_less = (a < b)  # False
    is_greater_equal = (a >= b)  # True
    is_less_equal = (a <= b)  # False

    # Logical Operators
    logical_and = (a > 0 and b > 0)  # True
    logical_or = (a > 0 or b < 0)  # True
    logical_not = not(a > 0)  # False

"""

def practicing_data_types():

    #Assing a integer to this variable
    int_number = 
    print("You changed int_number to: ", int_number)

    #Assing a float to this variable
    float_number = 
    print("You changed float_number to: ", float_number)

    #Assing a string to this variable
    string =
    print("You changed string to: ", string)

    #Assing a boolean to this variable
    boolean =
    print("You changed boolean to: ", boolean)

    #Assing a list to this variable use [elemen1, element2, element3]
    list_ =
    print("You changed list_ to: ", list_)

    #Assing a tuple to this variable use (elemen1, element2, element3)
    tuple_ =
    print("You changed tuple_ to: ", tuple_)

    #Assing a dictionary to this variable use {key1: value1, key2: value2}
    dict_ =
    print("You changed dict_ to: ", dict_)

    #Assing a set to this variable use {element1, element2, element3}
    set_ =
    print("You changed set_ to: ", set_)

    #Assing None to this variable
    none_ =
    print("You changed none_ to: ", none_)


def main():
    #Calling the function above
    practicing_data_types()
    


#You will see this often in python programs to call the main function
#This calls the main function when you run the program
if __name__ == '__main__':
    main()


