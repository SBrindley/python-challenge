# Start by asking to read the file
import os

#Module to read the file
import csv

#find the csv file to read

PyBankcsvpath = os.path.join("Resources", "budget_data.csv")

# Create the variables to hold the data needed for the report

Count = 0
Profit_total = 0
Profit_change = 0
Starting_Profit = 0
Change_list = []
Average_change = 0
Greatest_increase = ["", 0]
Greatest_decrease = ["", 0]

with open(PyBankcsvpath, 'r', encoding= "utf") as csvfile:
   
   
#read the file and declare the delimiter is ,
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    print(f"This is the header: {csv_header}\n")

    first_row = next(csvreader) 
    Count += 1
    Profit_total += int(first_row[1])
    Previous_total = int(first_row[1])
    for row in csvreader:
        print(row[0])
        Count +=1
        Profit_total += int(row[1])
        Profit_change = int(row[1]) - Previous_total
        Previous_total =int(row[1])
        Change_list += [Profit_change]
        Month = str(row[0])
        if Profit_change > Greatest_increase[1]:
            Greatest_increase[1] = Profit_change 
            Greatest_increase[0] = Month
        if Profit_change < Greatest_decrease[1]:
            Greatest_decrease[1] = Profit_change 
            Greatest_decrease[0] = Month
Average_change = sum(Change_list)/len(Change_list)
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {Count}")
print(f"Total:  ${Profit_total}")
print(f"Average Change: ${Average_change}")
print(f"Greatest Increase in Profits: {Greatest_increase}")
print(f"Greatese Decrease in Profits: {Greatest_decrease}")

#write results to new path -with open(PyBankcsvpath, 'w', encoding= "utf") as txtfile:
output_path = os.path.join("analysis", "budget_data_output.txt")

with open(output_path, 'w') as outfile:

        outfile.write("Financial Analysis\n")
        outfile.write("--------------------\n")
        outfile.write(f"Total Months: {Count}\n")
        outfile.write(f"Total:  ${Profit_total}\n")
        outfile.write(f"Average Change: ${Average_change}\n")
        outfile.write(f"Greatest Increase in Profits: {Greatest_increase}\n")
        outfile.write(f"Greatese Decrease in Profits: {Greatest_decrease}\n")









