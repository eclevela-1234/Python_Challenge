import os
import csv

# Path to file to collect data
csv_path = os.path.join('Resources', 'budget_data.csv')

# Define Variables
old_PL = 0
Average_Change = 0.00
Total_Trans = 0 
counter = 0
old_PL = 0
new_PL = 0
Change_Total = 0
row_max = 0
max_tally = 0
min_tally = 0
# gather data from file and save
with open(csv_path) as File:   
    bank_data = csv.reader(File)
    
    for row in bank_data:
        # Calculate number of months
        # Total_Months = sum(1 for row in (bank_data))
        if counter > 0:
            
            # get profit/loss value from table
            new_PL = int(row[1])
            
            # add new pay to total_trans
            Total_Trans = int(new_PL) + Total_Trans 
            # calculate month to month change 
            if counter > 2:
                Change_Total = abs(int(old_PL) - int(new_PL))
           
            # calculate max and min 
            if new_PL > max_tally:
                max_PL = (row[0] + " \n ($" + row[1] + ")")
                max_tally = new_PL
            if new_PL < min_tally:
                min_PL = (row[0] + " \n ($" + row[1] + ")")
                min_tally = new_PL
         

        # store last profit loss value 
        old_PL = new_PL
        # advance iterator
        counter = counter + 1         
      
 # Calculate total months
Total_Months = counter - 1   

# Print Table
print()
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Trans}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {max_PL}")
print(f"Greatest Decrease in Profits: {min_PL}")
print()
print("Note - Absolute value used for average change calculation")

Average_Change = round((Change_Total/Total_Months), 2)

write_path = os.path.join('Resources', 'bank_data_analysis.txt')

with open(write_path,'w') as File:

    File.write(f"\n")
    File.write(f"Financial Analysis\n")
    File.write("------------------------------------\n")
    File.write(f"Total Months: {Total_Months}\n")
    File.write(f"Total: ${Total_Trans}\n")
    File.write(f"Average Change: ${Average_Change}\n")
    File.write(f"Greatest Increase in Profits: {max_PL}\n")
    File.write(f"Greatest Decrease in Profits: {min_PL}\n")
    File.write(f"\n")
    File.write(f"Note - Absolute value used for average change calculation")
