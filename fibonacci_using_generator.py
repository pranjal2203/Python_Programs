#program for fiboncci series using generators

#inputting value for fibonacci series
n=int(input("enter value upto which fibonacci series should be generated : "))
def fib(limit): 
      
    # Initialize first two Fibonacci Numbers  
    a, b = 0, 1
  
    # One by one yield next Fibonacci Number 
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
# Create a generator object 
x = fib(n) 
   
# Iterating over the generator object using for loop  
for i in fib(n):  
    print(i,end=" , ")