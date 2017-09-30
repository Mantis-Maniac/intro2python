class stuffs(object):
    def do(self):
        print("These are just stuffs")





class music(stuffs):
    def define(self):
        print("You listen to them for leisure")

class funk(music):
    def sound(self):
        print("It sounds funky.")

class dubstep(music):
    def sound(self):
        print("BOOM, WAHWAHWAHWAHWAH, WOWwwwwww!")

class video(stuffs):
    def define(self):
        print("You watch this thing.")

class film(video):
    def vision(self):
        print("You watch it with popcorns.")

class food(stuffs):
    def whatIsIt(self):
        print("You eat it.")

class pizza(food):
    def slices(self):
        print("Western people love it.")

def sound():
    print "gigigigigagagagagaga...."

sound()
seven = film()
pepperoni = pizza()
uptownFunk = funk()
uptownFunk.define()
seven.vision()
pepperoni.slices()
uptownFunk.sound()

