import csv
data=[
    ['name','age','course'],
    ['siddharth',21,'aiml'],
    ['bajarang',22,'cse']
]
with open("students.csv","w",newline="")as file:
    write=csv.writer(file)
    write.writerows(data)