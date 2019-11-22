import os 
import csv
# user input can be written here. 
with open(os.path.join("Resources", "budget_data.csv"), "r") as my_file:
    my_csv = csv.reader(my_file)
    # print(my_cvs) 
    header = next(my_csv)
    

# print("              " + " Financial Analisis " + "             ")
# print("---------------------------------------------------------")


