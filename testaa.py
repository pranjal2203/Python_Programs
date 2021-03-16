def decimal(n):
     for i in range(1,n+1):
          print(i,end=" ,")

def octal(n):
     ls=list([])
     for i in range(1,n+1):
          if(i<8):
               print(i)
          else:
               while(i/8!=0):
                    ls.append(i%8)
     print(ls[::-1],end=" ,")
     ls.clear()

def binary(n):
     ls=list([])
     for i in range(1,n+1):
          while(i/2==0):
               ls.append(i%2)
     print(ls[::-1],end=" ,")
     ls.clear()

n=int(input("enter a number : "))
#decimal(n)
#octal(n)
binary(n)