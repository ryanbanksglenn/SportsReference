#Ryan Banks Glenn
#SportsReference 2022 Internship Application

import json

from tabulate import tabulate

with open('SportsReference.json') as json_records:
    records = json.load(json_records)

Teams=['BRO', 'BSN', 'CHC', 'CIN', 'NYG', 'PHI', 'PIT', 'STL']

NumberOfTeams=len(Teams)

rows, columns = (NumberOfTeams+2, NumberOfTeams+1)
results=[]
for i in range(rows):
    column = []
    for j in range(columns):
        column.append(0)
    results.append(column)

j=1

while j<(NumberOfTeams+1):
	i=1
	while (i<NumberOfTeams+1):
		if i==j:
			results[j][i]='--'
		else:
			results[j][i]=(records[Teams[j-1]][Teams[i-1]]['W'])
		i=i+1
	j=j+1

j=0
i=1
while i<NumberOfTeams+1:
	results[j][i]=Teams[i-1]
	i=i+1

i=0
j=1
while j<NumberOfTeams+1:
	results[j][i]=Teams[j-1]
	j=j+1

j=NumberOfTeams+1
i=1
while i<NumberOfTeams+1:
	results[j][i]=Teams[i-1]
	i=i+1

results[0][0]='Tm'
results[NumberOfTeams+1][0]='Tm'


print(tabulate(results, tablefmt='fancy_grid'))
