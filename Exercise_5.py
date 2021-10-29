# Write a program that receives two inputs from the terminal (using input()).
# One input is an integer, the other is a string. If the length of the string is equal to the
# value of the integer, the program terminates. Otherwise the program will ask the user to provide
# another integer. The program will keep asking for a number, until the length of the string and the value
# of the integer match each other.
# Example: string = "hello", integer = 4, output --> "Please provide another number"
a = int(input("number:"))
b = input("word:")


while len(b) != a:
    print("Please provide another number" ,)
    a = int(input("new number:"))
else:
    print("the number and word coincide in length")

#FINISHED AND WORKS CORRECTLY, CHECKED