#import the os module to create file paths across operating system
import os

#import module for reading CSV files
import csv
from typing import Counter

file= os.path.join ("PyBank", 'Resources', 'budget_data.csv')

# initializing the titles and rows list
Months = []
Amount = []
Change = []

#read the CSV file
with open (file, 'r') as csvfile:
    
    #create a csv reader object
    csvreader = csv.reader(csvfile, delimiter =',')
    header=next(csvreader)
    print(header)


#extract each data row:
    for row in csvreader:
        Months.append(row[0])
        Amount.append(int(row[1]))
    for i in range(len(Amount)-1):
        Change.append(Amount[i+1]-Amount[i])
        #print(Months)

#Total Months
    Total_Months = len(Months)
    print (Total_Months)

#Greatest increase and decrease in Profits
    Dec_Profit= min(Amount)
    Inc_Profit = max(Amount)
    print(Dec_Profit, Inc_Profit)

    #calcluate total volume 

    Total_vol =sum(int(row[1])
    print(Total_vol)
    #Total_Volume = 0
    #profit =0
    #loss = 0

    #Amount = int(row[1])
    #if Amount >=0:
            #profit= profit + Amount 
    #elif Amount <0:
           # loss = loss + Amount
    #Total_volume = profit - loss
    
    #print(Total_volume)
        

    #Average Change Calculation
        ## calculate total change/change in inputs

    