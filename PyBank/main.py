import os
import csv
# Define Variables
# old_pay = 0
Average_Change = 0.00
Total_Trans = 0 
counter=0
old_pay = 0
new_pay = 0
Average_Change_Total = 0

# Path to file to collect data
csv_path = os.path.join('Resources', 'budget_data.csv')

# gather data from file and save
with open(csv_path, 'r') as File:   
    reader = csv.reader(File)
    
    for row in File:
        
        Total_Months = sum(1 for row in (reader))
        if counter > 0:
            # get profit loss value from table
            new_pay = row[1] 
            # add new pay to total_trans
            Total_Trans = Total_Trans + new_pay
            print(Total_Trans)
            
        
        # Calculate Average Change
        
           
    
    # add 1 to counter in For loop
    counter += 1    
# Print Table
Average_Change = Average_Change_Total/Total_Months
# print()
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Trans}")
print(f"Average Change: ${Average_Change}")
# print(f"Greatest Increase in Profits: {GI_Month} ({GI_AMT})")
# print(f"Greatest Decrease in Profits: {GD_Month} ({GD_AMT})")
