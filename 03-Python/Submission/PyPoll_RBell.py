import csv

rows = 0
csvpath = "02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

vt_ct_per_candidate = {}



with open(csvpath, encoding='utf-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
       
    csv_header = next(csvreader)

    print()
    print(f"CSV Header: {csv_header}") 

    for row in csvreader:
        #print(row)
        rows += 1
        candidate = row[2]

        if candidate in vt_ct_per_candidate.keys():
            vt_ct_per_candidate[candidate] += 1
        else:
            vt_ct_per_candidate[candidate] = 1

#print(vtrs_ch_candidate)
print("Election Results")
print("--------------------------")
print(f"Total Votes:  {rows}")
print("--------------------------")

for x in vt_ct_per_candidate:
    voter_percentage = vt_ct_per_candidate [x] / rows * 100
    voter_percentage = round(voter_percentage, 3)
    print(f"{x}:  {voter_percentage}%  ({vt_ct_per_candidate [x]})   ")
    
print("--------------------------")

winner = max(vt_ct_per_candidate, key=vt_ct_per_candidate.get)
print(f'Winner: {winner}')
    
# write election results to a text file
with open('Election_Results.text', 'w') as f:
    f.write("Election Results\n")
    f.write("----------------------\n")
    f.write(f"Total Votes:  {rows}\n")
    f.write("----------------------\n")

    for x in vt_ct_per_candidate:
        voter_percentage = vt_ct_per_candidate [x] / rows * 100
        voter_percentage = round(voter_percentage, 3)
        f.write(f"{x}:  {voter_percentage}%   ({vt_ct_per_candidate [x]})\n")
    f.write("------------------------\n")
    f.write(f'Winner: {winner}')
   