# Write a program that receives an input from the terminal (using input()).
# This input needs to be an integer. Assign it to a variable named "n". The program will 
# compute the product n*nn*nnn and print it on the screen.
# example: n = 5 output = 5*55*555 = 152625
n = int(input(""))

n1 = str(n)
n2 = n1+n1
n3 = n1+n1+n1

output = n*int(n2)*int(n3)
print(output)

#FINISHED AND WORKS CORRECTLY