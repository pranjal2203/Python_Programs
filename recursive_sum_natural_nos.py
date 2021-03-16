#program to print sum of natural numbers recursively


#recursive function for calculating sum of natural numbers 
def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
print("sum of first five natural numbers is : ",sum(5))
print()
print("sum of first ten natural numbers is : ",sum(10))
print()
print("sum of first twenty natural numbers is : ",sum(20))
