import os
import csv

# Path to file to collect data
csv_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
Khan_votes = 0
Khan_votes0 = 0.000
Correy_votes = 0
Correy_votes0 = 0.000
Li_votes = 0
Li_votes0 = 0.000
Tooley_votes0 = 0.000
Tooley_votes = 0
other_votes = 0
winner_count = [Khan_votes, Correy_votes, Li_votes, Tooley_votes]

winner_list = ["Khan", "Correy", "Li", "O'Tooley"]
counter = 0
x = 0
y = 0
# open and loop data
with open(csv_path) as File:
    elect_data = csv.reader(File)
    #  loop and tally votes
    for row in elect_data:
        if counter > 0:
            if row[2] == "Khan":
                Khan_votes = Khan_votes + 1
            if row[2] == "Correy":
                Correy_votes = Correy_votes + 1
            if row[2] == "Li":
                Li_votes = Li_votes + 1
            if row[2] == "O'Tooley":
                Tooley_votes = Tooley_votes + 1
    
                
        counter = counter + 1
# establish total_votes
total_votes = counter - 1
# calculate percentages
Khan_votes0 = round(((Khan_votes/total_votes) * 100), 3)
Correy_votes0 = round(((Correy_votes/total_votes) * 100), 3)
Li_votes0 = round(((Li_votes/total_votes) * 100), 3)
Tooley_votes0 = round(((Tooley_votes/total_votes) * 100), 3)
# select winner and match index to winner_list 
x = max(winner_count)    

# print summary table
print()
print(f"Election Results")
print("---------------------------")
print(f"Total Votes: {counter-1}")
print("---------------------------")
print(f"Khan: {Khan_votes0}% ({Khan_votes})")
print(f"Correy: {Correy_votes0}% ({Correy_votes})")
print(f"Li: {Li_votes0}% ({Li_votes})")
print(f"O'Tooley: {Tooley_votes0}% ({Tooley_votes})")
print("---------------------------")    
print(f"Winner: {winner_list[x]}")
print("---------------------------")
