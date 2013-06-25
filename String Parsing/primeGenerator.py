def primes():
    n = 2 # The first prime number.
    yield n
    n+= 1 # The first odd prime number is 3.
    yield n
    
    prime = True
    while True:
        n += 2 # The remaining primes are all odd. Skip evens.
        for divisor in range(3, n, 2): # Check against previous odd integers.
            if (n % divisor == 0):
                prime = False
        if prime == True:
            yield n
        prime = True
        
f = primes()
for n in range(20): print f.next(),
print
print f.next()
    
    