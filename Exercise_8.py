# Write a program that receives two inputs from the terminal (using input()).
# Both inputs need to be integers. Assign them, respectively to a variable named "m"
# and a variable named "n". The program will print on the terminal, the greatest common divisor (GCD)
# of the two numbers.
# Example: n = 10, m = 12, output = 2
# Hint1: use a list to contain the divisors of n and one to contain the divisors of m. Use the method append() 
# to add elements to the lists.
# Hint2: there is a very smart and quick implementation of this that can be found online. I'd recommend to try and 
# come up with your own version

def gcd(m,n):
    if(n==0):
        return m
    else:
        return gcd(n,m%n)
  
m = int(input("m:"))
n= int(input("n:"))
  
print ("The gcd of" , m , "and" , n , "is : ",end="")
print (gcd(m,n))

#FINISHED AND WORKS CORRECTLYX, CHECKED