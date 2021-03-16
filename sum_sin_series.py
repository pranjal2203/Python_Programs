#program to print sum of sin series


#importing math class
import math

#inputting values from user
x = int(input("Enter the value of x in degrees:"))
n = int(input("Enter the number of terms:"))


#defining a function that calculates the sum of sine series
def sin(x, n):
    sine = 0
    for i in range(n):
        sign = (-1)**i
        pi = 22/7
        y = x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine


print(round(sin(x, n), 2))