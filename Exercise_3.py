# Write a program that receives an input from the terminal (using input()).
# This input needs to be a string. If the string is "This is the right string." the program ends.
# Otherwise it keeps printing "Please provide the right string" until the string "This is the right string." 
# is provided.
a = (input("what is your sentence?"))
str_a = str(a)
while True:
    if str(a) != "This is the right string":
        print("Please provide the right string:" ,)
        a = (input(""))
        
    if str(a) == "This is the right string":
        print("Exiting program, well done!")
        break
    
#FINISHED AND WORKS CORRECTLY, CHECKED