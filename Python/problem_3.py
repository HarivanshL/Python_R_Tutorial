"""
    Turtorials almost over hang in there

    For this problem set were gonna go over loops

    Loops are very important in programming. It speeds up 
    automation significantly. Imagine you have to print out
    the numbers from 1 to 100. You can do this manually but
    it will take a long time. Instead you can use a loop to
    do this in a few lines of code.


    Below are some examples of loops:

# Example of a for loop
for i in range(1, 101):
    print(i)

# Example of a while loop
i = 1
while i <= 100:
    print(i)
    i += 1

    

# Example of a nested loop
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")


You can keep nesting loops but it significantly decreases performance
by multiple orders of magnitude. So be careful when using nested loops
"""


# Problem 1: Print the numbers from 1 to 100 using a for loop
def print_numbers(fifty):
   for index in range(fifty,101):
       print (index)
       #comment index += 1; this will increment one more time as well eg (50,52,54)
       #for loop already increments by one with for loop


# Problem 2: Print the numbers from 1 to 100 using a while loop
def print_numbers_while(num):
    while num <= 100:
        print(num)
        num += 1
        #comment num = num +1

# Problem 3: Print the multiplication table of a number
def multiplication_table(num):
    for i in range(1,num):
        for j in range (1, num):
            print(i*j)
    #j represents another index, we cant use i again since its already defined





fifty = 50
print_numbers(fifty)
print_numbers_while(fifty)
multiplication_table(12)