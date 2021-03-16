# abcdcdc
# cdc
# 2

str=input("enter string : ")
st=input("enter sub string : ")

#x=str.find(st)
#print(str[x+1:])

def count_str(str,st):
     c=0
     x=str.find(st)
     if(x == -1):
          print("Sub-String not found in the main string ")
     else:
          c=c+1
          str=str[x+1:]
          while(len(str) != 0):
               y=str.find(st)
               if(y != -1):
                    c=c+1
                    str=str[y+1:]               
               else:                    
                    print(c)
                    break
               

count_str(str,st)
