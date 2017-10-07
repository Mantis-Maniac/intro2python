import random
b = input("input number: ")
a = range(b)
random.shuffle(a)
print a
def bubble(a):
    num=0
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            num = num + 1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        print "      ****" + str(a)
    print(a)
    print(num)

print bubble(a)

