
#hcf of two nos

n=int(input("enter first number : "))
m=int(input("enter second number : "))

def fact(n):
     l=[]
     for i in range(2,n+1):
          if(n%i==0):
               l.insert(0,i)
     return(l)

l1=fact(n)
#print(l1)
l2=fact(m)
#print(l2)

for x in l1:
     if x in l2:
          print("HCF of the two number is : ",x)
          break
