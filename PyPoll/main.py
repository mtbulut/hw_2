import os
import csv

with open(os.path.join("Resources","election_data.csv"), "r") as in_file:
    in_csv = csv.reader(in_file)
    header = next(in_csv)
    print(header)





    print('Election Results')

    print("---------------------------")


    "Total Votes: 3521001"
    '-------------------------'
    'Khan: 63.000 % (2218231)'
    'Correy: 20.000 % (704200)'
    'Li: 14.000 % (492940)'

    'Tooley: 3.000% (105630)'
    '-------------------------'
    'Winner: Khan'
    '-------------------------'






