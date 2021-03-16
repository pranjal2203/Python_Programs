#program to print calendar of a specific month starting from user's choice


#inputting user's choice 
days = int(input('Enter number of days in month: '))
count = input('First week day of the month in abbreveations : ')

#creating a dictionary with keys as days of week and value as 0-6
weekdays = {'Su': 0, 'M': 1, 'T': 2, 'W': 3, 'Th': 4, 'F': 5, 'Sa': 6}

#printing the header of the calender which contains abbreviated weekdays
print('{:>3}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'
      .format('Su', 'M', 'T', 'W', 'Th', 'F', 'Sa'))

#printing the first day as per the user's input
print (weekdays[count]*4*' ' + '{:>3}'.format(1), end=' ')

#for loop for printing the rest of the month
for current_day in range(2, days+1):
    
    if (weekdays[count] + current_day  -1) % 7 == 0:
        print ()
    print ('{:>3}'.format(current_day ), end=' ')

