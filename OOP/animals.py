class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def eat(self):
        print("dog is eating .......")
    
class Cat(Animal):
    def run(self):
        print('cat runs slowly . ...')

class Plants(object):
    def root(self):
        print('It has a root')

class crysanthemum(Plants):
    def look(self):
        print("this is when daisy became more grown.")


juhua = crysanthemum()
juhua.look()
Wangcai = Dog()
Wangcai.run()
Wangcai.eat()
Xiaohua = Cat()
Xiaohua.run()

print type(Xiaohua)
print isinstance(juhua, crysanthemum)
print isinstance(Wangcai , Cat)

print dir("ABCDE")

print "ABCDE".__len__()
print "ABCDE".lower()
print dir(Wangcai)
Wangcai.run()
