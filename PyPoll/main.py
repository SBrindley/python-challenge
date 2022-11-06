import os

import csv

PyPollcsvpath = os.path.join("Resources", "election_data.csv")

Total_votes = 0
Candidate_list = []




with open(PyPollcsvpath, 'r', encoding= "utf") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    print(f"This is the header: {csv_header}\n")

    Total_votes += 1
    first_row = next(csvreader) 

    for row in csvreader:
        Total_votes += 1





print(f"Total Votes: {Total_votes}")
