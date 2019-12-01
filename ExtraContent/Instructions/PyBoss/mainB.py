
import csv
import numpy


# user input can be written here. 
with open( "employee_data.csv", "r") as in_file: 
    csv_reader = csv.DictReader(in_file)
    with open("up_employee_data.csv", "w") as out_file:
        fieldnames =["Emp ID","Name","DOB","SSN","State"]

        csv_writer = csv.DictWriter(out_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            # del line['State']
            csv_writer.writerow(line)

   

   
    # header1 = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
    # data = list(my_csv)
    # print(data) 

    

    # full_names = []
    # for name in data:
    #     full_name = name[1]
    #     full_names.append(full_name)
    #     for item in full_names:
    #         first_last = item.strip().split(" ")
    #         first_name = first_last[0]
    #         last_name = first_last[1]
            
   

    
