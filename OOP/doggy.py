class doggy(object):
   

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def myNameIs(self):
        print ('%s, %s, %s' % (self.name, self.age, self.color)) 

    def bark(self):
        print ("Wang Wang !!")

wangcai = doggy("Wangcai Masarchik", 17, "gold")
xiaoming = doggy("Ming Van Der Ryn", 16, "silver")
wangcai.myNameIs()
xiaoming.myNameIs()
xiaoming.bark()
