import random
guess=random.randint(1,100)
attempt=0
print("wellcome to number guessing game")

while True:
    num=int(input("enter number between 1 to 100 = "))
    attempt +=1
    
    if num<guess:
        print("your number is smaller ")
    elif num>guess:
        print("your number is greater  ")
    else:
        print("Congratulations! you guess a correct number ")
        print("in ",attempt,'attempts')
        
        break