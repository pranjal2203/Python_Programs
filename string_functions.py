#program to show various string functions


#declaring various string variables
str="program to show various string functions"
st="LEARNING BY PRACTICE"
s="   Hello     "

#printing the variables which are used for different operations 
print("the various string variables used for these different string operations are : ")
print(str)
print(st)
print(s)

print("")


print("program to show various string functions ")
print("")

#lower()
print("before using lower() : "+st)
print("use of lower : "+ st.lower())
print("_" * 50)
print("")

#upper()
print("before using upper() : "+str)
print("use of upper : "+ str.upper())
print("_" * 50)
print("")

#strip()
print("before strip : "+ s)
print("after strip : "+ s.strip())
print("_" * 50)
print("")

#replace()
print("before replacing : "+st)
print("after replacing : "+ st.replace("BY","with"))
print("_" * 50)
print("")

#title()
print("use of title : "+ str.title())
print("_" * 50)
print("")

#lstrip()
print("use of lstrip: "+s.lstrip())
print("_" * 50)
print("")

#rstrip
print("use of rstrip : "+s.rstrip())
print("_" * 50)
print("")

#find()
print("use of find : ")
x=str.find("to")
print(x)
print("_" * 50)