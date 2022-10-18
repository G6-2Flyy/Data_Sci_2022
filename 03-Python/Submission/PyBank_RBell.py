import csv

csvpath = "02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv"

rows = 0
total = 0

avg_chg  = 0
chngprofit = 0

avg_profChge = []

mthlyprofit = []

grIncnprofit = 0
grIncMonth = ""

grDecnprofit = 0
grDecMonth = ""

with open(csvpath, encoding='utf-8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # print(row)
        rows += 1
        total += int(row[1])

        if rows != 1:
            chngprofit = int(row[1]) - mthlyprofit
            avg_profChge.append(chngprofit)
            if chngprofit > grIncnprofit:
                grIncnprofit = chngprofit
                grIncMonth = row[0]
            elif chngprofit < grDecnprofit:
                grDecnprofit = chngprofit
                grDecMonth = row[0]
            else:
                pass
        
        mthlyprofit = (int(row[1]))

avg_chg = sum(avg_profChge)/len(avg_profChge)

# to perform terminal disply
print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months:  {rows}")
print(f"Total:  ${total}")
print(f"Average Change:  ${round(avg_chg, 2)}")
print(f"Greatest Increase in Profits:  ${grIncnprofit}")
print(f"Greatest Decrease in Losses:  ${grDecnprofit}")


# to generate a text file with results
with open('financial_analysis.text', 'w') as f:

    f.write("Financial Analysis\n")
    f.write("----------------------\n")
    f.write(f"Total Months:  {rows}\n")
    f.write(f"Total:  ${total}\n")
    f.write(f"Average Chage:  ${round(avg_chg,2)}\n")
    f.write(f"Greatest Increase in Profits:  ${grIncnprofit}\n")
    f.write(f"Greatest Decrease in Profits:  ${grDecnprofit}\n")