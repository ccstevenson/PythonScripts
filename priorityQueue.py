class priorityQueue:
    def __init__(self):
        self.priorityQueue = list()
        
    def add(self, val):
        val = val.split()
        
        value = val[0]
        priority = val[1]
        
        if self.priorityQueue:
            for (index, (thisValue, thisPriority)) in enumerate(self.priorityQueue):
                if int(priority) > int(thisPriority):
                    self.priorityQueue.insert(index, (value, priority))
                    return
            self.priorityQueue.append((value, priority)) # Add to the end of the list.
        else:
            self.priorityQueue.insert(0, (value, priority))
        
    def dump(self):
        for pair in self.priorityQueue:
            print(pair)
            
    def queueGenerator(self):
        for (value, priority) in self.priorityQueue:
            yield value
        
def test():
    yield 'Sally 2'
    yield 'Linsey 19'
    yield 'Joe 3'
    yield 'Bob 2'
    yield 'Christopher 10'
    yield 'John 1'
    yield 'Jane 5'
    yield 'Bob 0'
    yield 'Errol 10'
    yield 'Jill 5'
    yield 'Michael 7'
    yield ''
        
def expectedResult():
    yield 'Linsey'
    yield 'Christopher'
    yield 'Errol'
    yield 'Michael'
    yield 'Jane'
    yield 'Jill'
    yield 'Joe'
    yield 'Sally'
    yield 'Bob'
    yield 'John'
    yield 'Bob'
    yield ''
    
def assertTestResults():
    resultGenerator = expectedResult()
    queueGenerator = queue.queueGenerator()
    testVal = True
    
    for resultVal in queueGenerator:
        testVal = next(resultGenerator)
        assert testVal == resultVal 
        
    print("Debug flag enabled. Unit test ran.\n", 
          "Unit test passed. Results:", sep="")    

if __name__ == '__main__':
    testFlag = False
    import sys
    # An additional command-line parameter was supplied.
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d':
            testFlag = True

    userInputGenerator = test() # Testing generator object.
    queue = priorityQueue()
    inputVal = True
    while inputVal: 
        if testFlag == False: # The user has supplied input
            inputVal = input('Enter a space-separated pair: ')         
        else: # Use the unit test.
            inputVal = next(userInputGenerator)  
            
        if inputVal:
            queue.add(inputVal)
        
    if testFlag:
        assertTestResults()
        
    queueGenerator = queue.queueGenerator()
    for val in queueGenerator:
        print(val)