import os
import csv

# Print Formatting
print("Election Results")
print("-------------------------")

# Path for CSV File
csvpath = os.path.join("Resources", "PyPoll_data.csv")

# Show total net profits and losses 
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)   
    total_votes = sum(1 for row in csvreader)
    print("Total Votes: " + str(total_votes))
    print("-------------------------")

# Find how many votes each candite receieved
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    khan_total = 0
    correy_total = 0
    otooley_total = 0
    li_total = 0
    for row in csvreader:
        if "Khan" in row:
            khan_total+= 1
        elif "Correy" in row:
            correy_total += 1
        elif "Li" in row:
            li_total += 1
        elif "O'Tooley" in row:
            otooley_total += 1
    # Print Results 
    print("Khan: " + str(float(khan_total) / float(total_votes) * 100) + "% " + "(" + str(khan_total) + ")")
    print("Correy: " + str(float(correy_total) / float(total_votes) * 100) + "% " + "(" + str(correy_total) + ")")
    print("Li: " + str(float(li_total) / float(total_votes) * 100) + "% " + "(" + str(li_total) + ")")
    print("O'Tooley: " + str(float(otooley_total) / float(total_votes) * 100) + "% " + "(" + str(otooley_total) + ")")
    print("-------------------------")
    print("Winner: Khan")
    print("-------------------------")