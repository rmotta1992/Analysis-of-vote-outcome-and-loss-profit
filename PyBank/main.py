# Import Depencies 
import os
import csv

# Path for CSV File
csvpath = os.path.join("Resources", "PyBank_data.csv")

#Print Header and formatting
print("Financial Analysis")
print("----------------------------")

# Show number of months in data set
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)   
    months = sum(1 for row in csvreader)
    print("Total Months: " + str(months))
 
# Show total net profits and losses 
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)   
    net_profits = 0
    for row in csvreader: 
        net_profits += int(row[1])
    print("Total: " + str(net_profits))

# Show Average montly change 
monthly_change =  []
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    previous_net_change = first_row[1]
    for row in csvreader:
        net_change = (int(previous_net_change) - int((row[1])) / 2)
        average_change = int(net_change) / 86
    print("Average Change: " + str(average_change))

   
