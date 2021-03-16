'''program to print the pattern
1
23
456
78910
'''

#initialinzing variables
n=1
r=4  
s=2

#starting nested for loop to print pattern
for i in range(r):
    for j in range(1,s):
        print(n, end=' ')
        n += 1
    print("")
    s=s+1