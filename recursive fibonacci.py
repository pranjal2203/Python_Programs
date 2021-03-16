#program to print fibonacci series using recursion


#recursive function for generating fibonacci series
def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  

#input from the users
no = int(input("Enter the terms: "))  

#checking if the input is correct or not  
if no <= 0:   
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(no):  
       print(FibRecursion(i),end=" ")