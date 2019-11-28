import os 
import csv
import numpy
import math

# user input can be written here. 
with open(os.path.join("Resources", "budget_data.csv"), "r") as my_file:
    my_csv = csv.reader(my_file)
    # print(my_cvs) 
    header = next(my_csv)
    data = list(my_csv)
    # print(data)                   
    
    count =0
    for month in data:
        count += 1

    all_amount = []
    for num in data:
        amount = num[1]
        all_amount.append(int(amount))

    # sorted_amount = sorted(all_amount)
    average_change = (int(data[-1][1]) - int(data[0][1]))/count
    # average_change = sum(all_amount)/count

        # print(all_total)    

    print("Financial Analisis")
    print("-"* 30)
    print(f'Total months: {count}')
    print(f'Total: {sum(all_amount)}')
    print(average_change)
    


