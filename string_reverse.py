#program to print string in reverse


#input a string from the user
str= input("enter a string to be processed : ")
print("original string : ",str)
st=str.split(' ') #splitting string
rev=' '.join(reversed(st)) #reversing the string
print("string after reversal : ",*st[::-1])
