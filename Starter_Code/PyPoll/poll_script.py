import os
import csv

# reads file
csvpath = os.path.join('Resources', 'election_data.csv')

vote_count = 0
candidate_catalouge = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        vote_count += 1
        if row[2] in candidate_catalouge:
            candidate_catalouge[row[2]] += 1
        else:
            candidate_catalouge[row[2]] = 1


print("Elction results")
print()
print(f"Total votes: {vote_count}")
print()

max_percentage = 0

for candidate, votes in candidate_catalouge.items():
    percentage = votes/vote_count
   
    print(f"{candidate}: {percentage: .2%}, with a total of  {vote_count} votes")

    if percentage > max_percentage:
        max_percentage = percentage
    if votes == max(candidate_catalouge.values()):
        winner = candidate
print()    
print(f"Our winner is: {winner} with {max_percentage: .0%} of the votes!!")

output_path = os.path.join("election_results.csv")

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



