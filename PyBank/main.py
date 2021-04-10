import os
import csv

# Path to file to collect data
csv_path = os.path.join('Resources', 'budget_data.csv')

# Define Variables
old_pay = 0
Average_Change = 0.00
Total_Trans = 0 
counter = 0
old_pay = 0
new_pay = 0
Average_Change_Total = 0
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
            new_pay = int(row[1])
            
            # add new pay to total_trans
            Total_Trans = int(new_pay) + Total_Trans 
            # calculate month to month change 
            if counter > 2:
                Average_Change_Total = abs(int(old_pay) - int(new_pay))
           
            # calculate max and min 
            if new_pay > max_tally:
                max_pay = (row[0] + " \n ($" + row[1] + ")")
                max_tally = new_pay
            if new_pay < min_tally:
                min_pay = (row[0] + " \n ($" + row[1] + ")")
                min_tally = new_pay
         

        # store last profit loss value 
        old_pay = new_pay
        # advance iterator
        counter = counter + 1         
      
 # Calculate total months
Total_Months = counter - 1   
# Print Table
Average_Change = round((Average_Change_Total/Total_Months), 2)

print()
print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Trans}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {max_pay}")
print(f"Greatest Decrease in Profits: {min_pay}")

