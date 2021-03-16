#count and display no of goats n ducks by counting by their headds n feets


#inputing value of no of heads and legs
head=int(input("enter the number of heads : "))
legs=int(input("enter the number of legs : "))

#for loop for calculating no of goats and ducks
for duck in range(1,head):
    goat=head-duck
    tot=4*goat+2*duck
    if(tot==legs):
        print("total number of goats : ",goat)
        print("total number of ducks : ",duck)