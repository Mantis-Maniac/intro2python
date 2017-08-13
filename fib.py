def fib(n):
    a, b, c = 0, 0, 1
    while a < n:
        print c 
        b, c = c, b + c
        a = a + 1
fib(12)
