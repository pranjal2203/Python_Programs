#importing the required libraries
import numpy as np
import pandas as pd

#setting the value manually
arr =np.array([0.15,0.12,0.35,0.38,0.55,0.56,0.57,0.75,0.77,0.9,0.94])

#declaring the bins upon which the distribution will take place
bins = [0.0, 0.2, 0.4, 0.6, 0.8,1.0]

#using inbuilt function digitize to birfurcate the datapoints
bin_indices = np.digitize(arr, bins)
unique, counts = np.unique(bin_indices, return_counts=True)

#initializing the count variables
acount,bcount,ccount,dcount,ecount = 0,0,0,0,0

#loop which divides the datapoints into their respective bins 
#and counting the number of values in each bin too and printing the values to be displayed
for ele in arr:
    if ele > 0.0 and ele < 0.2 and acount >= 0 and acount <= min(counts)-1:
        print(ele,end=" ")
        acount +=1
    elif ele > 0.2 and ele < 0.4 and bcount >= 0 and bcount <= min(counts)-1:
        print(ele,end=" ")
        bcount +=1
    elif ele > 0.4 and ele < 0.6 and ccount >= 0 and ccount <= min(counts)-1:
        print(ele,end=" ")
        ccount +=1
    elif ele > 0.6 and ele < 0.8 and dcount >= 0 and dcount <= min(counts)-1:
        print(ele,end=" ")
        dcount +=1
    elif ele > 0.8 and ele < 1.0 and ecount >= 0 and ecount <= min(counts)-1:
        print(ele,end=" ")
        ecount +=1
    else:
        count = 0