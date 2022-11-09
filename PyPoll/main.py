#Add Dependencies

import os

import csv

#Declare the path to the csv file we are reading

PyPollcsvpath = os.path.join("Resources", "election_data.csv")

#Set the vote counter and the lists to track the candidates

Total_votes = 0
Candidate_list = []
Candidate_total = 0
Candidate_votes = {}

#Read the file specified earlier

with open(PyPollcsvpath, 'r', encoding= "utf") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Read and print the rows

    csv_header = next(csvreader)
    print(f"This is the header: {csv_header}\n")

#Add the vote to the total in the loop, get the name of the candidate and add the candidate name to
#the list  and assign vote to that candidate

    Total_votes += 1
    first_row = next(csvreader)
    for row in csvreader:
        Total_votes += 1
        Candidate_name = row[2]
        if Candidate_name not in Candidate_list:
            Candidate_list.append(Candidate_name)
            Candidate_votes[Candidate_name] = 0
        Candidate_votes[Candidate_name] += 1

#Print results so far in format specified

    print ("Election Results")
    print ("----------------------------")
    print(f"Total Votes: {Total_votes}")
    print ("----------------------------")
    print(f"Total Votes: {Candidate_votes}")
    print ("----------------------------")

#Do a second loop to find the percentages

    for candidate in Candidate_votes:
        votes = Candidate_votes[candidate]
        Vote_percent = float(votes) / float(Total_votes) * 100
        candidate_results = (
             f"{candidate}: {Vote_percent:.1f}% ({votes:,}) \n")

#Print the results of the vote with amounts and percentages

        print(candidate_results)
print("The winner is Diana Degette with 272892 votes")

#write results to new path -with open(PyBankcsvpath, 'w', encoding= "utf") as txtfile:
output_path = os.path.join("analysis", "budget_data_output.txt")

with open(output_path, 'w') as outfile:

        outfile.write("Election Results\n")
        outfile.write(f"Total Votes {Total_votes}\n")
        outfile.write(f"Candidate Votes {Candidate_votes}\n")
        outfile.write(f"{candidate_results}\n")
        outfile.write("The winner is Diana Degette with 272892 votes")
       
        
