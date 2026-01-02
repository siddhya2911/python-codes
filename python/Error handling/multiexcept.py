try:
    a=int(input('enter value'))
    b=int(input('enter second value'))
    print("division =",a/b)
    
except ZeroDivisionError:
    print('we can not divide by zero')
except ValueError:
    print('invalid values')
else:
    print("execute successfully")
# except(ZeroDivisionError,ValueError):
#     print("error occurred")