#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    """ Returns employee info in a list """

    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    with open (csv_file_location) as handle:
        reader = csv.DictReader(handle, dialect = 'empDialect') 
        employee_list = list(reader)
        return employee_list

def process_data(employee_list):
    """ Returns number of employee per department """

    department_data = {}
    for row in employee_list:
        dept_name = row['Department']
        department_data[dept_name] = department_data.get(dept_name, 0) + 1 
    return department_data

def write_report(dictionary, report_file):
    """ Writing  per department info in a file """
    
    with open(report_file, 'w+') as handle:
        for key,value in dictionary.items():
            handle.write(str(key) + ":" + str(value) + "\n")

employee_list = read_employees('employee.csv')

department_data = process_data(employee_list)

write_report(department_data,'report.txt' )
