#inout=i am giving interviwew at 12pm

st="I am giving the interview at 12"
s=list(st.split(' '))


#print("the noumber of words in the sentence is = ",len(s))

dict={}
key=[]
value=[]
for x in s:
     dict[x]=s.count(x)
print(dict)


for x in s:
     if(x.isdigit()):
          print(x)

     



     

#for x in s:
#     if(x.isdigit()==True):
#          print(x)



