class stack:
    def __init__(self): 
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

def octal(decNumeros):
    a = stack()
    
    while decNumeros > 0:
        remainder = decNumeros % 8
        a.push(remainder)
        decNumeros /= 8

    bin = ''
    
    while a.isEmpty() == False:
        bin += str(a.pop())
    return bin

print octal(123)
