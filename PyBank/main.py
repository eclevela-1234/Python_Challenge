# Importing necessary tools
import os
import csv


# Path to file to collect data
csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path, newline='') as File:  
    reader = csv.reader(File)
    # num_rows = 0
    print("")
    print("Financial Analysis")
    print("--------------------------")
    for row in File:

        Total_Months = sum(1 for row in (reader))
        print(f"Total Months: {Total_Months}")

        Total_Profit_Loss = sum( for row in (reader))
        print(f"Total: {Total_Profit_Loss}")
