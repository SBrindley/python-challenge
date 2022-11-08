
import os

import csv
PyPollcsvpath = os.path.join("Resources", "election_data.csv")
Total_votes = 0
Candidate_list = []
Candidate_total = 0
Candidate_votes = {}
with open(PyPollcsvpath, 'r', encoding= "utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"This is the header: {csv_header}\n")
    Total_votes += 1
    first_row = next(csvreader)
    for row in csvreader:
        Total_votes += 1
        Candidate_name = row[2]
        if Candidate_name not in Candidate_list:
            Candidate_list.append(Candidate_name)
            Candidate_votes[Candidate_name] = 0
        Candidate_votes[Candidate_name] += 1


print ("Election Results")
print ("----------------------------")
print(f"Total Votes: {Total_votes}")
print ("----------------------------")
print(f"Total Votes: {Candidate_votes}")
print ("----------------------------")
print (f"Candidate total {Candidate_total}")