import os
import csv
import pprint
import math


with open(os.path.join("Resources","election_data.csv"), "r") as in_file:
    in_csv = csv.reader(in_file)
    header = next(in_csv) # activating this will exculede the firs line. 
    data = list(in_csv)
    # print(data)

###################################################
    count = 0
    for row in data:
        count += 1
    

    print('Election Results')

    print("---------------------------")
    print("Total votes: " + str(count))
    print("---------------------------")

####################################################

    candidate_names = []

    for row in data:
        if row[2].strip() not in candidate_names:

            candidate_names.append(row[2])
        else:
            continue
    print(candidate_names)

    total_vote_khan = 0
    for row in data:
        if row[2] == candidate_names[0]:
            total_vote_khan +=1
    print(f"{candidate_names[0]}: {(total_vote_khan/count)*100} % ({total_vote_khan}) ")

    total_vote_Correy = 0
    for row in data:
        if row[2] == candidate_names[1]:
            total_vote_Correy +=1
    print(f"{candidate_names[1]}: {(total_vote_Correy/count)*100} % ({total_vote_Correy}) ")

    total_vote_li = 0
    for row in data:
        if row[2] == candidate_names[2]:
            total_vote_li +=1
    print(f"{candidate_names[2]}: {(total_vote_li/count)*100} % ({total_vote_li}) ")

    total_vote_Tooley = 0
    for row in data:
        if row[2] == candidate_names[3]:
            total_vote_Tooley +=1
    print(f"{candidate_names[3]}: {(total_vote_Tooley/count)*100} % ({total_vote_Tooley}) ")

# who is the winner?
    print('-------------------------------------')

    if max(total_vote_Correy,total_vote_khan,total_vote_li) == total_vote_khan:
        print(f'Winner: {candidate_names[0]}') 
    elif max(total_vote_Correy,total_vote_khan,total_vote_li) == total_vote_Correy:
        print(f'Winner: {candidate_names[1]}')
    else:
        print(f'Winner: {candidate_names[2]}')

    print('--------------------------------------')

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






