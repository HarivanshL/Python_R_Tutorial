"""
    You made it!

    One of the best utilities of Python is the ability to use functions.
    Functions are a way to encapsulate code that you want to reuse.
    You can define a function using the def keyword.

    You will have seen this in the previous problems, but now you will create your own function.

    
    For this problem you only have to write two functions


"""

# Function 1
# Write a function called 'add' that takes in a list and returns the sum of all the elements in the list
def add(list):
    total = 0
    for index, element in enumerate(List):
        print(index, " ", element)
        total += element
    #print("sum=", total)

    sum =0
    for i in range(0, len(List)):
        sum += List[i]
    #print(sum)
    return sum

    

# Function 2
# Write a function called 'multiply' that takes two arguments and returns the product of the two arguments
def multiply(product1,product2):
    print(product1*product2)


if __name__ == "__main__":
    # Test your functions here
    

    List = [10,20,30,40]
    output = add(List)
    print("output", output)
    print("sum=",add(List))

    product1 = 100
    product2 = 200
    multiply(product1,product2)
    #multiply(product1=100,product2=200), another way to write the condition