print('1. Addition\n2. Subtraction\n3. Multiplication\n4. Division')
a=float(input('Enter first number ='))
b=float(input('Enter second number ='))
choice = int(input('Enter your choice ='))
if choice==1:
    print('Addition =',a+b)
elif choice==2:
    print('Subtraction =',a-b)
    
elif choice==3:
    print('Multiplication =',a*b)
elif choice==4:
    if b==0:
        print("Error you can't divide by zero")
    else:
        print('Division=',a/b)
else:
    print('Enter a valid choice')
