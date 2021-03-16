#program to print pattern using generator
# 1
# 12
# 123 
# 1234





#below program for checking isogram words
str=input("enter a word to be checked : ")
str.lower()
def split(s):
    return[char for char in s]
#print(split(str))
l1=split(str)
l2=[]
for elem in l1:
    q=1
    if(l1.count(elem) > 1):
        print("not")
        break 