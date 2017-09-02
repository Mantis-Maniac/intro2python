def add(x,y):
    return x + y  
#print add(3,4)

print reduce(add, [1,3,5,7,9,11])

def fn(x,y):
    return x*10 + y

print reduce(fn, [1,3,5,7,9])
