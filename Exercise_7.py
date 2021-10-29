# Write a program that receives one input from the terminal (using input()).
# The input needs to be an integer. The program will compute the factorial of 
# this number and print it on the screen. If the number is negative the program will print 
# "Factorial does not exist for negative numbers". Remember that the factorial of 0 is 1.
# Example: input = 5, output = 5*4*3*2*1 = 120

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)

a = int(input(""))

if a < 0:
    print("Factorial does not exit for negative numbers")
if a == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", a,"is:", factorial(a))

#FINISHED AND WORKS CORRECTLY, CHECKED