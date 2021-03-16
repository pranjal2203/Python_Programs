#program to extract domain name from url


#inputting the url for the user
url=input("enter the url : ")
a=url.find(".") #finding the first . used in the input
b=url.rfind(".") #finding the second . used in the input
st=url[a+1:b] #slicing
print("Domain is : "+st)
