class animal:
    def show(self):
        print('cat')
class cat(animal):
    def show(self):
        print('meow')
o=cat()
o.show()
o.show()