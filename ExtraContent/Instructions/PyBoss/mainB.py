
import csv
import numpy
import datetime

Emp_ID = []   # format NOT needed
First_Name = []   # format needed
Last_Name = []    # format needed
DOB = []  # format needed
SSN = []   # format needed
State = []  # This is done 

state_abbr = { 
    'Alabama': 'AL',
    'Alaska':'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

# user input can be written here. 
with open( "employee_data.csv", "r") as in_file: 
    csv_reader = csv.reader(in_file)
    
    # skipping the hearder
    header = next(csv_reader)   
    data = list(csv_reader)
      
    for line in data:
            
        Emp_ID.append(line[0]) 
    # print(Emp_ID) 

    full_names = []
    for row in data:
        full_name = row[1]
        full_names.append(full_name)
        for item in full_names:
            first_last = item.strip().split(" ")
            first_name = first_last[0]
            last_name = first_last[1]
        First_Name.append(first_name)
        Last_Name.append(last_name)

    # print(First_Name)
    # print(Last_Name)
    # orginizing the date time.
        dob_Formatted = datetime.datetime.strptime(row[2], '%Y-%m-%d')
        dob_Formatted = dob_Formatted.strftime('%m/%d/%Y') 

        DOB.append(dob_Formatted)    
    # print(DOB)
        formated_ssn = list(row[3])
        # for row in formated_ssn: 
        formated_ssn[0:3]= ("*", "*", "*")
        formated_ssn[4:6] = ("*", "*")
        f_ssn = "".join(formated_ssn)

        SSN.append(f_ssn)
    # print(SSN)
        row(4)
   

    
