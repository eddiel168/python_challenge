import os
import csv
# import numpy as numpy

#def column(matrix, i):
#    return[row[i] for row in matrix]


row = 0
with open('election_data.csv') as pypollcsv:
    csv_read = csv.reader(pypollcsv, delimiter=',')
#   print(csv_read)
    line_count = 0
#   column(csv_read,3)
    csvdata=[]


    candidate=[]
    for row in csv_read:
        if line_count == 0:
            csvdata.append(row)
# test to see if data below are correct
#            print(csvdata)
#            print(candidate)
#            print(row[2],"Row 2")
            line_count +=1
        else:
            line_count +=1
            candidate.append(row[2])

#    for trow in t_csv_read:

print(f'Total lines = {line_count}.')

output = []
for x in candidate:
    if x not in output:
        output.append(x)
# test to see if data below are correct
# print(output)

for cname in output:
    print(f'{cname} has {candidate.count(cname)} votes')
    print(f'  which is {int(100*candidate.count(cname)/line_count)}%')

