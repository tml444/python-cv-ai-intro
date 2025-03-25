# This script shows some basic python functions

# print a string (a string is a text)
print("Hello")

# save string to a variable and print the variable content
my_text = "Hello my text!"
print(my_text)

# create a while loop that iterates as long as counter is below 10
counter = 0
while counter < 10:
    
    # Note: everything that happens in the while loop has to be indented by 1 tab
    print(counter)
    counter = counter + 1
    
print("while loop ended")
print("Counter state: ", counter)
    
# get input from the user over console
print("Type in Number A and press Enter:")

a = input() # this waits for the user to type in some string and press enter, then saves the string to the variable a
a = float(a) # we cannot calculate with a string, so 'a' must be converted to the data type float (a decimal number)

print("Type in Number B and press Enter:")

b = input()
b = float(b)

# perform simple math by creating a function with the keyword "def" that multiplies two values a and b
def multiply(number_a, number_b):
    
    result = number_a * number_b
    
    return result

# use the defined function by giving it the two variables a and b as input arguments
product = multiply(a, b)

print("The product of a and b is: ")
print(product)

# analyse the product with a simple if statement

if product > 100:
    
    print("The product of a and b is greater than 100.")
    
elif product == 100:
    
    print("The product of a and b is equal to 100.")
    
else:
    
    print("The product of a and b is smaller than 100.")