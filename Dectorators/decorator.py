def fcount(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    wrapper.__name__ = func.__name__
    return wrapper

# Test code
@fcount
def f(n):
    return n+2

for n in range(5):
    print f(n)
    
print 'f count =',f.count

@fcount
def g(n):
    return n*n
print 'g count =',g.count
print g(3)
print 'g count =',g.count

''' Output:
2
3
4
5
6
f count = 5
g count = 0
9
g count = 1
'''


