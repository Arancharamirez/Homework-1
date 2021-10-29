# Write a program that receives two inputs from the terminal (using input()).
# Both inputs need to be an integer. Assign them, respectively to a variable named "n"
# and a variable named "p". The program will 
# compute the product n*nn*nnn*...*nnn...n (where the last number contains n written p number of times)
# and print it on the screen.
# example 1: n = 5, p = 4, output = 5*55*555*5555 = 152625
# example 2: n = 3, p = 6, output = 3*33*333*3333*33333*333333 = 1220864470355308779


def multiplication(n,p):
    str_n=str(n)
    multiplication = n
    multiplication_of_all_strings = str(n)
    for i in range(1,p):
        multiplication_of_all_strings = multiplication_of_all_strings + str_n
        multiplication = multiplication * int(multiplication_of_all_strings)
    return multiplication

n = int(input("n:"))
p = int(input("p:"))

mul_of_no = multiplication(n,p)
print("mul:",mul_of_no)

#FINISHED AND WORKS CORRECTLY, CHECKED
