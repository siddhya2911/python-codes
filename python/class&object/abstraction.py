from abc import ABC, abstractmethod
class hide(ABC):
    def show(self):
        pass
    
class square(hide):
    def display(self):
        print('area=side*side')
        pass
o=square()
o.display()
o.show()