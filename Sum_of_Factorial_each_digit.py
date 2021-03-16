#program to print sum of factorial of each digit of a number



#input choice of user
no=int(input("enter a number : "))


#defining function for calculating sum of factorial of a digit
def fact(n):
    facto=1
    while(n!=0):
        facto=facto*n
        n=n-1
    return facto


#declare a variable for calculating total sum of each digit
sum=0


#while loop that extracts each digit of the entered number, send it to function fact() and adds the factorial
while(no!=0):
    d=int(no%10)
    sum=sum+fact(d)
    no=no//10
print("the sum of factorial of each digit is : ",sum)#printing sum