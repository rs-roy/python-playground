#!/usr/bin/env python3

import csv
import re

def replace_domain(address, old_domain, new_domain):
    """ returns updated email domain list """
    updated_list = []
    pattern = r'@[\S]+'
    for item in address:
        check_domain = re.search(pattern,item)
        if check_domain.group() == old_domain:
            new_address = item.replace(old_domain, new_domain)
            updated_list.append(new_address)
        else:
            updated_list.append(item)
    return updated_list
    
def main():
    old_domain = "@abc.edu"
    new_domain = "@xyz.edu"
    name_list = []
    current_email_list = []
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    with open('email.csv') as handle:
        reader = csv.DictReader(handle, dialect = 'empDialect')
        for row in reader:
            name_list.append(row['Full Name'])
            current_email_list.append(row['Email Address'])

    updated_address_list = replace_domain(current_email_list, old_domain, new_domain)

    with open('updated_email.txt', 'w+') as handle:
        handle.write("Full Name" + ", " + "Email Address" + "\n")
        for i,j in zip(name_list,updated_address_list):
            handle.write(str(i) + ", " + str(j) + "\n")

if __name__ == "__main__":
    main()
