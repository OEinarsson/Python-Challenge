import os
import csv

# reads file
csvpath = os.path.join('Resources', 'election_data.csv')

#simple variables to track candidates and total votes 
vote_count = 0
candidate_catalouge = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# logs candidates and tracks their respective votes
    for row in csvreader:
        vote_count += 1
        if row[2] in candidate_catalouge:
            candidate_catalouge[row[2]] += 1
        else:
            candidate_catalouge[row[2]] = 1

# prints total votes to terminal
print("Elction results")
print()
print(f"Total votes: {vote_count}")
print()

# tracks highest percentage achieved
max_percentage = 0

# loops through catalouge to figure out their percentage of votes print them out
for candidate, votes in candidate_catalouge.items():
    percentage = votes/vote_count
   
    print(f"{candidate}: {percentage: .2%}, with a total of  {vote_count} votes")

# checks and establishes highest percentage
    if percentage > max_percentage:
        max_percentage = percentage

# selects winner
    if votes == max(candidate_catalouge.values()):
        winner = candidate
print()   
print(max_percentage) 
# print(f"Our winner is: {winner} with {max_percentage: .0%} of the votes!!")
if max_percentage > 70:
    print(f"Our winner, by a landslide is {winner} with an astonishing {max_percentage: .0%} of the votes!!")
elif max_percentage > 60:
    print(f"The crowd favorite today is {winner} with {max_percentage: .0%} of the votes!!")
else:
    print(f"Our winner today is: {winner} with {max_percentage: .0%} of the votes!!")

# establishes output file
output_path = os.path.join("election_results.csv")

# writes to output file 
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Elction results"])
    csvwriter.writerow([])
    csvwriter.writerow([f"Total votes: {vote_count}"])
    csvwriter.writerow([])

    

    for candidate, votes in candidate_catalouge.items():
        percentage = votes/vote_count
   
        csvwriter.writerow([f"{candidate}: {percentage: .2%}, with a total of  {vote_count} votes"])

        if percentage > max_percentage:
            max_percentage = percentage
        if votes == max(candidate_catalouge.values()):
            winner = candidate
    csvwriter.writerow([])    
    csvwriter.writerow([f"Our winner is: {winner} with {max_percentage: .0%} of the votes!!"])   



