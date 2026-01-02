# with open("data.txt","r")as file:
#     reading = file.read()
#     print(reading)
    
# read line by line 
# with open("data.txt","r")as file:
#     for line in file:
#         print(line.strip())


#read all line as a list
with open("data.txt","r")as file:
    line=file.readlines()
    print(line)