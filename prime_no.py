#program to print all prime number between 100 and 500


#for loop for the limit 100-500 
for x in range(100,500):
    c=0
    #for loop for checking prime number
    for i in range(2,(x//2+1)):
        if(x % i==0):
            c=c+1
            break
    if(c==0 and x!=1):#if no is not divisible by any other no nor it's 1 then print it
     print(x,end=" , ")
