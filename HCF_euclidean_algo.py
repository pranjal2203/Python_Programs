#program for HCF euciledian algorithm


#input  2 numbers from the  user to calculate the hcf
a=int(input("enter a number : "))
b=int(input("enter another number smaller than the previously entered number : "))


#function for calculating the euciledian algorithm 
def hcf(x,y):
    while y:
        temp = y
        y = x %y
        x = temp
    return x
print(hcf(a,b))