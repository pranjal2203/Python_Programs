'''program to print the pattern
1
11
111
1111
'''

#nested for loop for printing pattern

for i in range(0,5):
         for j in range(0, i+1):
              print("1 " , end="")
         print("\r")