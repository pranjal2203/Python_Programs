#frequency of one element in a string

st=input("Enter a string : ")
s=input("Enter the element whose frequency is to be found out : ")
print("The frequency of ",s," in ",st," is : ",st.count(s))

#using for loop 

#fre=0
#for ele in st:
#     if(ele==s):
#          fre=fre+1
#print("The frequency of ",s," in ",st," is : ",fre)


#frequency of each element in a string

for i in st:
     print("frequency of ",i,"in ",st,"is : ",st.count(i))
          
