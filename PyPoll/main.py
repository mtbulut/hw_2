import os
import csv

with open(os.path.join("Resources","election_data.csv"), "r") as in_file:
    in_csv = csv.reader(in_file)
    header = next(in_csv)

###################################################
    count = 0
    for row in in_csv:
        voter = row[0]
        count +=1

    data = list(in_csv)
    # print(data[0:5])
    clean_data = [[int(e.strip()) for e in row] for row in data if row[2].strip() == 'khan']
    print(clean_data)



    print('Election Results')

    print("---------------------------")
    print("Total votes: " + str(count))






###############################################################################

    "Total Votes: 3521001 DONE with THIS"
    '-------------------------'
    'Khan: 63.000 % (2218231)'
    'Correy: 20.000 % (704200)'
    'Li: 14.000 % (492940)'

    'Tooley: 3.000% (105630)'
    '-------------------------'
    'Winner: Khan'
    '-------------------------'






