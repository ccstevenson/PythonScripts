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
            
def consume(supp):
    import sys
    supp.next
    charcount = 0
    for val in supp:
        for char in val:
            if (charcount % 3 != 0):
                sys.stdout.write(char)
            else:
                sys.stdout.write(' ')
                sys.stdout.write(char)
            charcount += 1
        supp.next
        
consume(produce('A2B5E3426FG0ZYW3210PQ89R'))
    