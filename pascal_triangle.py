#program to print pascal triangle



#defining function that generates pascal triangle
def pascal(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(function(i,j)," ", end="")
        print()


#function which determine how the triangle will be displayed
def function(n,k):
    c=1
    if (k >n-k):
        k=n-k
    for i in range(0, k):
        c=c*(n-i)
        c=c//(i+1)
 
    return c

#inputting value of trianlge and calling the function
n=int(input("enter value upto which pascal's triangle is to be generated : ")) 
pascal(n)