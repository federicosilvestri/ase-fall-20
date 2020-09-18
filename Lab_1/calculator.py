# calculator.py

def sum(m,n):
    i = 0
    n = abs(n)
    
    while i <= n:
        m += 1
        i += 1
    
    return m
    
def divide(m,n):
    isNegative = (m < 0 and n > 0) or (m > 0 and n < 0)
    m = abs(m)
    
    if n == 0:
        # no!
        raise Exception("Division by zero!")
    d = 0
    
    while m > 0:
        m -= n
        d += 1
    return d
        
        
    
        
print(divide(8,4))