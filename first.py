class Person:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    
    def greeting(self):
        print('저는 {}입니다.'.format(self.name))

minseo=Person('minseo','Seoul')
minseo.greeting() 