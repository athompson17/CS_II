def p(a, b):
    if b > 0:
       return a + p(a,(b-1))
    else:
       return 0

a = 0
b = 0
a = input('give a number')
b = input('give another number')
a = int(a)
b = int(b)
print(p(a,b))