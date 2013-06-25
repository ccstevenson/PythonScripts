def produce(s):
    printedNext = 0
    for index, char in enumerate(s):
        if printedNext == 1:
            printedNext = 0
            pass
        elif char.isdigit():
            printedNext = 1
            yield (int(char)+1) * (s[index + 1])
        else:
            yield char

p = produce('A2B5E3426FG0ZYW3210PQ89R')
for s in p: print s,
print