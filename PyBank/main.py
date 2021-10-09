#import the os module to create file paths across operating system
import os

#import module for reading CSV files
import csv
#from typing import Counter

file= os.path.join ('PyBank', 'Resources', 'budget_data.csv')

# initializing the titles and rows list
Months = []
Amount = []
Change = []

#creation of additional variable
Total_months= 0
Dec_profit = 0
Inc_profit = 0


#read the CSV file
with open (file, 'r') as csvfile:
    
    #create a csv reader object
    csvreader = csv.reader(csvfile, delimiter =',')
    header=next(csvreader)
    #print(header)


#extract each data row:
    for row in csvreader:
        Months.append(row[0])
        Amount.append(int(row[1]))
    for i in range(1, len(Amount)):
        Change.append((int(Amount[i])-int(Amount[i-1])))

#total Months
    Total_months = len(Months)
    #print(Total_months)
#Max and Min in changes of profit/losses
    Dec_profit= min(Change)
    Inc_profit= max(Change)
#Pull indexes of Max and Min
    Mon_inc= Change.index(max(Change))+1
    Mon_dec = Change.index(min(Change))+1

#print data to terminal
print(f"Financial Analysis")
print("----------------------------------")
print(f"Total Months: {len(list(Months))}")
print(f"Total: ${sum(Amount)}")
print(f"Average Change: ${round(sum(Change)/len(Change), 2)}")
print(f"Greatest Increase in Profits: {Months[Mon_inc]} (${(Inc_profit)})")
print(f"Greatest Decrease in Profits: {Months[Mon_dec]} (${(Dec_profit)})")

#output to a text file
output = os.path.join ("Pybank", 'output.txt')
with open(output, "w") as new:
   new.write("Financial Analysis")
   new.write("\n")
   new.write("----------------------------------")
   new.write("\n")
   new.write(f"Total Months: {len(Months)}")
   new.write("\n")
   new.write(f"Total: ${sum(Amount)}")
   new.write("\n")
   new.write(f"Average Change: ${round(sum(Change)/len(Change), 2)}")
   new.write("\n")
   new.write(f"Greatest Increase in Profits: {Months[Mon_inc]} (${(Inc_profit)})")
   new.write("\n")
   new.write(f"Greatest Decrease in Profits: {Months[Mon_dec]} (${(Dec_profit)})")
 