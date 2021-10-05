#import the os module to create file paths across operating system
import os

#import module for reading CSV files
import csv

# os.chdir(os.path.dirname("election_data.csv"))
elect_data = os.path.join("PyPoll","Resources", "election_data.csv")

#read the CSV file
with open (elect_data, 'r') as csvfile:

    #create a csv reader object
    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvfile)

    # initializing the titles and rows list
    Voters_candidates = []
    Voters_per_candidate = []

    #extract field names, first row
    fields = next(csvreader)
    #extract each data row:
    for row in csvreader:
        Voters_candidates.append(row)



print()