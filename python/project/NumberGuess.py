import random
guess=random.randint(1,100)
attempt=0
print("wellcome To Number Guessing Game")
print("Try to guess the number between 1 to 100 ")
while True:
    num=int(input("enter number = "))
    attempt +=1
    
    if num<guess:
        print("your number is smaller ")
    elif num>guess:
        print("your number is greater  ")
    else:
        print("Congratulations! you guess a correct number ")
        print("in ",attempt,'attempts')
        
        break