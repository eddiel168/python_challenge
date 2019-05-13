import os
import csv
row = 0
with open('budget_data.csv') as pybankcsv:
    csv_read = csv.reader(pybankcsv, delimiter=',')
#   print(csv_read)
    total = 0
    line_count = 0
    for row in csv_read:
        if line_count == 0:
# print the columns out
#           print(f'Column names are {", ".join(row)}')
            line_count +=1
        else:
# print the data out

#find change
            if line_count == 1:
                previous = int(row[1])
                changetot = 0
                
            else:
#               change = int(row[1])/denom
#               changetot += change
#               changeprev = change
                if line_count == 2:
                    change = int(row[1])-previous
                    changetot += change
                    changeprev = change
                    previous = int(row[1])
                    grtincchg = 0
                    grtdechg = 0

                else:
                    change = int(row[1]) - previous
                    if change > grtincchg:
                        grtincdat = row[0]
                        grtincchg = change
                        previous = int(row[1])
                    else: 
                        if change < grtdechg:
                            grtdecdat = row[0]
                            grtdecchg = change
                        else:
                            previous = int(row[1])
#        
#           print(f'\t{row[0]}, {row[1]}.')
            line_count +=1
            total += int(row[1])
#           print sum(row[1] for row in csv_read)

# print # of month
    print(f'Total # of months {line_count}.')
    print(f'Total amount is ${total}.')
    print(f'Average Change is {changetot/(line_count-1)}')
    print(f'Greatest increase date is {grtincdat} at P&L of ${grtincchg}.')
    print(f'Greatest decrease date is {grtdecdat} at P&L of ${grtdecchg}.')

