class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def parchecker(symbolString):
    s = Stack()
    for i in symbolString:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.isEmpty():
                return False
            else:
                s.pop()

    return s.isEmpty()



#print parchecker('((((((((')
  

def divideBy2(decNumber):
    a = Stack()

    while decNumber > 0:
        remain = decNumber % 2
        a.push(remain) 
        decNumber /= 2
          
    bin = ''
    
    while a.isEmpty() == False:
        bin += str(a.pop())
    return bin

print divideBy2(10)  
