#program to find total number of mangoes



k=1

#while loop for calculating no f mangoes
while(True):
    i=k
    if(i/3 >1 and i%3==1):
        num1=int(i/3)
        i=i-int(i/3)-1
    elif(i/3 >1 and i%3==1):
        num2=int(i/3)
        i=i-int(i/3)-1
    elif(i/3 > 1 and i%3==1):
        num3=int(i/3)
        i=i-int(i/3)-1
print(num1,num2,num3)

