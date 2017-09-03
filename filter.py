def is_odd(n):
    return n % 2 == 1

#print is_odd(3)

print filter(is_odd, range(100))
