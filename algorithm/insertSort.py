a = [3,4,1,2,5]

def insertSort(a):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp 
            print "    ****" + str(a)
        print a

    return a

    
       
print insertSort(a)
