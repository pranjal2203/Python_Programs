'''program to print the pattern
1
22
333
4444
'''

#initializing variable
x=0

#for loop
for i in range(0,5):
    x=x+1 
    for j in range(0,i+1):
        print(x , end=" ") 
    print("\r")