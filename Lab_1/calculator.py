# calculator.py

def sum(m,n):
    i = 0
    s = -1 if n < 0 else 1
    
    while i < abs(n):
        i += 1        
        m += s
        
    return m
    
def divide(m,n):
    isNegative = (m < 0 and n > 0) or (m > 0 and n < 0)
    m = abs(m)
    n = abs(n)
    
    if n == 0:
        # no!
        raise Exception("Division by zero!")
    d = 0
    
    while m > 0:
        m -= n
        d += 1
    return d
        
        
    
        
print(sum(-1,4))