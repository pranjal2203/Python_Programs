#program to input day month n year and print it in a normal format


#inputting day, month and year from the user
year=int(input("enter year : "))
month=int(input("enter month between 1 to 12 : "))
day=int(input("enter day between 1 to 31 : "))

#fuction for printing month in string
def mon(month):
    if(month==1):
        return("Of January,")
    elif(month==2):
        return("Of February,")
    elif(month==3):
        return("Of March,")
    elif(month==4):
        return("Of April,")
    elif(month==5):
        return("Of May,")
    elif(month==6):
        return("Of June,")
    elif(month==7):
        return("Of July,")
    elif(month==8):
        return("Of August,")
    elif(month==9):
        return("Of September,")
    elif(month==10):
        return("Of October,")
    elif(month==11):
        return("Of November,")
    elif(month==12):
        return("Of December,")

#function for printing date        
def date(day):
    if(day==1 or day==21 or day==31):
        return("st")
    elif(day==2 or day==22):
        return("nd")
    elif(day==3 or day==23):
        return("rd")
    else:
        return("th")

#printing the whole date in normal written format        
print(day,date(day),mon(month),year,end="")