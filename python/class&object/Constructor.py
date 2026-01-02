# The constructor is a special method that runs automatically when an object is created.

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
s1=student('siddharth',2)
print('my name =',s1.name)
print('my roll no. =',s1.rollno)