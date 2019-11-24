import os
import csv
import pprint


with open(os.path.join("Resources","election_data.csv"), "r") as in_file:
    in_csv = csv.reader(in_file)
    header = next(in_csv)
    print(header)

###################################################
    count = 0
    for row in in_csv:
        count += 1
    data = list(in_csv)

####################################################

    candidate_names = []

    for row in in_csv:
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
        else:
            continue
    print(candidate_names)




    # print(candidate_names)
    print(candidate_names)

    # for candidate in candidate_names:





    # clean_data = [[e for e in row] for row in data if row[2].strip() == 'Khan']
    # # print(clean_data)
    #
    # sorted_data = max(clean_data, key=lambda row: row[1])  # row[1] yerine ayni sekilde sum(row[2]) yazilabilir.
    #
    # pprint.pprint(sorted_data)


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






