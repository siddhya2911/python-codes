# class bike:
#     def __init__(self,speed,brand):
#         self.speed=speed
#         self.brand=brand
    
#     def myfun(self):
        
#         print(self.brand,self.speed)
# b1=bike(300,'ninja')
# b1.myfun()
class bike:
    def myfun(self,speed,brand):
        self.speed=speed
        self.brand=brand
        print(self.brand,self.speed)
b1=bike()
b1.myfun(300,'ninja')