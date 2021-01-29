import math

error = 0
    
def create(n, d):
    if d == 0:
        error = -1
        return (None, None)
    return (n,d)

def clear_error():
    error = 0

def add(a, b):
    try:
        if a[1] == b[1]:
            n = a[0]+b[0]
            d = a[1]
        else:
            n = a[0]*b[1] + b[0]*a[1]
            d = a[1]*b[1]
        return (n,d)
    except:
        error = -1
        return (None, None)

def sub(a, b):
    try:
        if a[1] == b[1]:
            n = a[0]-b[0]
            d = a[1]
        else:
            n = a[0]*b[1] - b[0]*a[1]
            d = a[1]*b[1]
        return (n,d)
    except:
        error = -1
        return (None, None) 

def div(a,b):
    try:
        if(type(a)==int):
            a=(a,a)
        if(type(b)==int):
            b=(b,b)
        n = a[0]*b[1]
        d = a[1]*b[0]
        return(n,d)
    except:
        error = -1
        return (None, None)

def mul(a, b):
    try:
        n = a[0] * b[0]
        d = a[1] * b[1]
        return(n,d)
    except:
        error = -1
        return (None, None) 

def inp():
    try:
        n,d = [int(i) for i in input().split()]
        return (n,d)
    except ValueError:
        error = -1
        print("Not enough values to unpack / too many values to unpack (expected 2)")
        return (None, None) 

def eq(a,b):
    a = _GCD_reduce(a)
    b = _GCD_reduce(b)
    if(a==b):
        return True
    return False

def It(a,b):
    f = a[0] * b[1]
    s = b[0] * a[1]
    if f < s:
        return True
    return False
            
def prt(a):
    print((a[0], a[1]))

def _GCD_reduce(a):
    k = math.gcd(a[0], a[1])
    n = a[0] // k
    d = a[1] // k
    return (n,d)
