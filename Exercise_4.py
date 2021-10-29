# Write a program that receives three inputs from the terminal (using input()).
# These inputs needs to be integers. The program will print on the screen the sum of these three inputs.
# However, if two of the three inputs are equal, the program will print the product of these three inputs.
# Example 1: n = 1, m = 2, l = 3, output = 1 + 2 + 3 = 6
# Example 2: n = 1, m = 2, l = 2, output = 1 * 2 * 2 = 4
n = int(input("n:"))
m = int(input("m:"))
l = int(input("l:"))


if n != m != l:
    output1 = n + m + l
    print(output1)
elif n == m or n == l or m ==l:
    output2 = n * m * l
    print(output2)

#FINISHED AND WORKS CORRECTLY, CHECKED