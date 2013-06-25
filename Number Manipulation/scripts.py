# Part 1

def sequenceEval():
   x = []
   line = raw_input()
   while line:
      x.append(line)
      line = raw_input()

   # Cast contents of x to integers
   for index, val in enumerate(x): x[index] = int(val)

   if x == []: print 'No numbers were entered.'
   else:
      print 'The list entered is:', x
      print 'The sum is:', sum(x)
      print 'The minimum is:', min(x)
      print 'The maximum is:', max(x)
      print 'The median is:', median(x)
      print 'The average is:', average(x)

def average(x):
   total = 0.0
   for val in x:
      total += val
   return (total / len(x))

def median(x):
   x.sort()
   if (len(x) % 2) != 0: # List length is odd
      middleIndex = ((len(x) - 1) / 2)
      return x[middleIndex]
   else: # list length is even
      middle1 = x[(len(x) / 2) - 1]
      middle2 = x[(len(x) / 2)]
      median = (middle1 + middle2) / 2.0
      return median

# Part 2

class Stack(object): # Could also inherit from list as shown in textbook.
   def __init__(self): self.theStack = []
   def push(self, toAdd): self.theStack.append(toAdd)
   def pop(self): self.theStack.pop()
   def top(self): return self.theStack[-1]
   def size(self): return len(self.theStack)

# Part 3

def num(n):
   number = 1
   count = 0
   while count < (n-1):
      count += 1
      number += (count + 1)
   return number

# Part 4

import math
def mysqrt(a,g):
   xNext = (g + (a/g)) / 2.0
   error = abs(xNext - g)
   xPrev = xNext
   n = 1 # Two guesses required to compute error. Will always iterate once.

   while error >= 0.00005:
      xNext = (xPrev + (a/xPrev)) / 2.0
      error = abs(xNext - xPrev)
      xPrev = xNext
      n += 1

   print 'Number of iterations:', n
   return xNext

# Testing

print 'Part one.'
sequenceEval() 

print '\nPart two.'
myStack = Stack()
for val in range(1,11,1): myStack.push(val)

for val in range(1,11,1):
   print myStack.top()
   myStack.pop()

print '\nPart three.'
for val in range(1, 11, 1): print num(val)

print '\nPart four.'
sqrtResult = mysqrt(57, 5)
print 'Result of mysqrt(57,5):', sqrtResult
print 'The difference between answers:', abs(sqrtResult - math.sqrt(57))
