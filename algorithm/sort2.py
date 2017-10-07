import random

i = range(100)
random.shuffle(i)

def insert(m):
    for j in range(len(m)-1):
        for k in range(j+1, len(m)):
            if m[j] > m[k]:
                temp = m[j]
                m[j] = m[k]
                m[k] = temp
            print "      ****" + str(m)
        print m
    return m

print insert(i)
