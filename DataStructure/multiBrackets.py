class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        return self.items.pop()


def parchecker2(stringBrackets):
    s = Stack()
    for i in stringBrackets:
        if i == '(' or  i == '[' or i == '{' :
            s.push(i)
        elif i == ')' or i == ']' or i == '}':
            if s.isEmpty():
                return False
            else:
                s.pop()
    
    return s.isEmpty()
        
print parchecker2('[[[[[]]]]]')
        
        
        
