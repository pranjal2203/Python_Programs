#string format conversion what is s,r and a?


#declaring various string variables
str="Pranjal"
st="Pathak"
s="CDAC"


# !s is used to call str() on  values which in turn return a string version of the object
print("first name :{val!s}".format(val=str))


# !r is used to call repr() on values which in turn return a string containing a printable representation of object
print("last name :{val!r}".format(val=st))


# !a is used to call ascii() on values whihc in turn return a string containing a printable representation
# of objects in ascii characters 
print("college :{val!a}".format(val=s))
