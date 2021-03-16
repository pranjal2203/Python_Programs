#program to print fibonacci series

#initializing variables
a,b,count=0,1,0

#inputting value for series
n=int(input("enter number of fibonacci terms to be generated : "))


#printing first two elements of fibonacci series
print(a,b,end=" ")
while count < n:
    c=a+b
    a, b=b, c
    print(c,end=" , ")
    count=count+1
