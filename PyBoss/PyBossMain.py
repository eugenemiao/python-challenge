import os
import csv

pyboss_path_1 = os.path.join('employee_data1.csv')
pyboss_data = []

with open(pyboss_path_1) as csvfile:
    pyboss_reader = csv.DictReader(csvfile)
    print(pyboss_reader)

    for row in pyboss_reader:
        pyboss_data = [row]

#Splitting name to first and last name
for row in pyboss_data:
    emp = row["Emp ID"]
    
    name = row["Name"]
    new_name = name.split(" ")
    first_name = new_name[0]
    last_name = new_name[1]
    print(first_name)
    print(last_name)

#Splitting DOB to rearrange it
    dob = row["DOB"]
    split_dob = dob.split("-")
    month = split_dob[1]
    day = split_dob[2]
    year = split_dob[0]
    new_dob = month + "/" + day + "/" + year
    print(new_dob)

#splitting SSN and convering first 5 digits into **    
    ssn = row["SSN"]
    split_ssn = ssn.split("-")
    first_ssn = split_ssn[0]
    split_ssn[0] = '***'
    second_ssn = split_ssn.insert(1,"**")
    split_ssn[1] = '**'
    third_ssn = split_ssn[2]
    new_ssn = str(first_ssn) + "-" + str(second_ssn) + "-" + third_ssn
    print(new_ssn)

#changing state to abbreviation
    state = row["State"]
    state_path = os.path.join('States.py')
    state.append(us_state_abbrev)

    #adding new data to info provided?
    """pyboss_data.append({
        "Emp ID" = emp,
        "First Name" = first_name,
        "Last Name" = last_name,
        "DOB" = new_dob
        "SSN" = new_ssn,

    })"""




