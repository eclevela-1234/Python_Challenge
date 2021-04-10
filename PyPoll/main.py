import os
import csv

# Path to file to collect data
csv_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
Khan_votes = 0
Khan_votes0 = 0
Correy_votes = 0
Correy_votes0 = 0
Li_votes = 0
Li_votes0 = 0
Tooley_votes0 = 0
Tooley_votes = 0
other_votes = 0
winner = 0
counter = 0


# open and loop data
with open(csv_path) as File:
    elect_data = csv.reader(File)

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
    # print(Khan_votes)







# print summary table
print()
print(f"Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"Khan: ({Khan_votes})")
print(f"Correy: ({Correy_votes})")
print(f"Li: ({Li_votes})")
print(f"O'Tooley: ({Tooley_votes})")
print("---------------------------")    
print(f"Winner: {winner}")
print("---------------------------")
