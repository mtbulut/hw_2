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
    for row in data:
        count += 1

    all_amount = []
    for num in data:
        amount = num[1]
        all_amount.append(int(amount))

    all_month = []
    for num in data:
        month = num[0]
        all_month.append((month))
    

   
    # average_change 
    average_rate_change = round((all_amount[-1] - all_amount[0])/(count -1))

    difference_rows_inc =[]
    for i in range(len(all_amount)-1):
        dif = all_amount[i+1] - all_amount[i] 
        difference_rows_inc.append(dif)
    max_difference_row = max(difference_rows_inc)
    min_difference_row = min(difference_rows_inc)

    
    inc_month = all_month[(difference_rows_inc.index(max_difference_row))+1]
    
    dec_month = all_month[(difference_rows_inc.index(min_difference_row))+1]
   
    
    # print()
    print("Financial Analisis")
    print("-"* 30)
    print(f'Total months: {count}')
    print(f'Total: ${sum(all_amount):,}')
    print(f"Average Change: ${average_rate_change:,}")
    print(f"Greatest Increase in Profits: {inc_month } ${max_difference_row:,}")
    print(f"Greatest Decrease in Profits: {dec_month }${min_difference_row:,}")
    


