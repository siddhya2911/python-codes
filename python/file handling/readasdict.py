import csv
with open("students.csv","r")as file:
    read=csv.DictReader(file)
    for row in read:
        print(row)