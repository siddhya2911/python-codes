# import csv
# with open("students.csv","r") as file:
#     r=csv.reader(file)
#     for row in r:
#         print(row)

import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for index, row in enumerate(reader):
        if index == 1:    
            print(row)
