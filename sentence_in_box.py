#program to print sentence in a box


#inut from the user
str=input("enter a short sentence : ")


#displaying parameters of the  box
print("_"*53)
for i in range(0,3):
    print("|"," "*50,"|")
print("|"," "*10,str,)
for j in range(0,3):
    print("|"," "*50,"|")
print("|","_"*50,"|")
