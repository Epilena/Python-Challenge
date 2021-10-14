#import the os module to create file paths across operating system
import os

#import module for reading CSV files
import csv

# os.chdir(os.path.dirname("election_data.csv"))
elect_data = os.path.join("PyPoll","Resources", "election_data.csv")

#read the CSV file
with open (elect_data) as csvfile:

    #create a csv reader object
    csvreader = csv.reader(csvfile) 
    
    csvheader = next(csvreader)

    # initializing the titles and rows list
    Voters_ID = []
    County = []
    Candidate = []
    Votes = 0
    CandidateVotes={}

    #read through each data row:
    for row in csvreader:
        #total vote count
        Votes = Votes+1
        #candidate voted for
        candidate_name= row[2]
        #create loop to tally candidate voted for
        if candidate_name not in CandidateVotes:
            CandidateVotes[candidate_name] = 1
            Candidate.append(candidate_name)
        else:
    
        #add votes to candidate's total count
            CandidateVotes[candidate_name]+=1
        #CandidateVotes[candidate_name]+=1
    cand_res_list = []
    for name, vote in CandidateVotes.items():
        result= name
        vote_perc = float(vote)/float(Votes) *100
        cand_res_list.append(f"{name}: {vote_perc:.2f}% ({vote:,})")

    #determining overall winner
        
            
#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {Votes}")
print("--------------------------")
for name2 in cand_res_list:
    print(name2)
print("---------------------------")
#print(f"Winner: {}")
#print("---------------------------")

