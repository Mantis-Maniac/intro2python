a = [5,4,2,1,3]

def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1] :
                a[j] , a[j+1] = a[j+1] , a[j]
            print "    ***" + str(a)
        print a
    return a

print bubbleSort(a)
