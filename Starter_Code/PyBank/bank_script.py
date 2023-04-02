import os
import csv

# sets path for csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# starting variables
total_profit = 0 
change_counter = 0
greatest_increase = {"month": "A",
            "value": 0}
greatest_decrease = {"month": "A",
            "value": 0}
last_month = 0
change_total = 0

# loops through the data to calculate totals, increase, decreases and month counts
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        change_counter += 1
        month = row[0]
        this_month = int(row[1])
        total_profit += int(this_month)
        change = this_month - last_month
        # skips first line of data, and saves last months value for change calculation
        if change_counter > 1:
            change_total += change
            last_month = this_month
        
        # step to adjust for change average
        else: 
            change_total -= this_month
        
        # tracks the greatest increase and decrease of change
        if change > greatest_increase["value"]:
            greatest_increase["value"] = change
            greatest_increase["month"] = month
        if change < greatest_decrease["value"]:
            greatest_decrease["value"] = change
            greatest_decrease["month"] = month
        
# calculates average change and rounds it to a dollar value for readability
change_average = round(change_total / (change_counter - 1), 2)

# prints to terminal
print("Financial Analysis")

print("______________________")
print("              Total Months:  " + str(change_counter))
print("                     total: $" + str(total_profit))
print("            Average Change: $" + str(change_average))
print("greatest_increase Increase: $" + str(greatest_increase["value"]) + ", " + str(greatest_increase["month"]))
print(" greatest_increase Decrese: $" + str(greatest_decrease["value"]) + ", " + str(greatest_decrease["month"]))

# writes an all information to a financial analysis csv within the same folder
output_path = os.path.join("financial_analysis.csv")

# opens file and writes each line
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])

    csvwriter.writerow(["______________________"])
    csvwriter.writerow(["              Total Months:  " + str(change_counter)])
    csvwriter.writerow(["              Total Profit: $" + str(total_profit)])
    csvwriter.writerow(["            Average Change: $" + str(change_average)])
    csvwriter.writerow(["Greatest Increase: $" + str(greatest_increase["value"]) + ", " + str(greatest_increase["month"])])
    csvwriter.writerow([" Greatest Decrese: $" + str(greatest_decrease["value"]) + ", " + str(greatest_decrease["month"])])
