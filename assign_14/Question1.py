import csv
# read csv

file=open('MarvellousInfosystems_PlayPredictor.csv')

csvreader=csv.reader(file)

header=[]
header=next(csvreader)
print(header)

rows=[]
for row in csvreader:
    rows.append(row)
    
print(rows)