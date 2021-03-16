#program to print sum of cos series


#importing math class
import math

#inputting values from user
x = int(input("Enter the value of x in degrees:"))
n = int(input("Enter the number of terms:"))

#defining a function that calculates the cosine seires sum

def cosine(x, n):
    cosx = 1
    sign = -1
    for i in range(2, n, 2):
        pi = 22/7
        y = x*(pi/180)
        cosx = cosx + (sign*(y**i))/math.factorial(i)
        sign = -sign
    return cosx
print(round(cosine(x, n), 2))