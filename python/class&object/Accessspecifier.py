# 3 main access specifiers in Python are:
# 1. Public Access Specifier =(eg. name) accessible from anywhere 
# 2. Protected Access Specifier=(eg. _name) accessible within the class and its subclasses
# 3. Private Access Specifier=(eg. __name) accessible only within the class
class public_class:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def mydata(self):
        print('name=',self.name)
        print('mark=',self.mark)
        print('\n')
p1=public_class('abhishek',80)
print(p1.name)
print(p1.mark)
p1.mydata()

#protected
print("Protected")
class employee:
    def __init__(self):
        self._salary=4000000
    def show(self):
        print('my first salary=',self._salary)
class p_employee(employee):
    def display(self):
        print('my protected salary=',self._salary)
        print('\n')
e1=p_employee()
e1.show()
e1.display()

#private
print('Private')
class Bank:
    def __init__(self):
        self.__balance = 10000   

    def show_balance(self):
        print("Balance:", self.__balance)
        
b = Bank()
b.show_balance()