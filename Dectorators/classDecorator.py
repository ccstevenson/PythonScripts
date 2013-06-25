class fcount(object):
    def __init__(self, f, *args, **kwargs):
        self.func = f
        self.count = 0
        self.withcount = None
    def __call__(self, *args, **kwargs):
        self.count += 1
        if self.withcount is not None: # then executing within the with
            self.withcount += 1
        return self.func(*args, **kwargs)
    def __enter__(self):
        self.withcount = 0
        return self
    def __exit__(self, a, b, c):
        print "with block count = %d" % self.withcount
        return True
    

# Test code
@fcount
def f(n):
    return n+2

for n in range(5):
    print f(n)
print 'f count =',f.count

def foo(n):
    return n*n

with fcount(foo) as g:
    print g(1)
    print g(2)
print 'g count =',g.count
print 'f count =',f.count

with fcount(f) as g:
    print g(1)
    print g(2)
print 'g count =',g.count
print 'f count =',f.count

''' Output:
2
3
4
5
6
f count = 5
1
4
with block count = 2
g count = 2
f count = 5
3
4
with block count = 2
g count = 2
f count = 7
'''