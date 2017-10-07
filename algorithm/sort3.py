import random
a = range(100)
random.shuffle(a)
print a


def select(x):
    for i in range(len(x)-1):
        min_index = i
        for j in range(i+1, len(x)):
            if x[min_index] > x[j]:
                min_index = j
        if min_index != i:
            x[min_index], x[i] = x[i], x[min_index]
            print "    ****" + str(x)
    return x
    print x

print select(a)





