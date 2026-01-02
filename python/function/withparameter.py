def myfun(a,b):
    print('addition =',a+b)
    return 0   
myfun(10,20)

def myfun2(c,d):
    return c-d
result=myfun2(20,10)
print("substraction= ",result)

def str(name='bade'):
    print(name)
    return 0
str()
str('siddharth')

def total(*num):
    return sum(num)
print(total(1,2,3))

add=lambda x,z:x+z
print(add(2,2))
