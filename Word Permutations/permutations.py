# Part one

with open("words.txt","r") as f:
    words = set(word.rstrip() for word in f)

from itertools import permutations
def allwords(s, n=1):
    perm = list()
    while len(s) >= n:
        p = permutations(s, n)
        for i in p:
            i = ''.join(i)
            i = i.lower()
            if i in words and i not in perm:
                perm.append(i)
        n += 1
    # Python sort is stable, so will be left in alphabetical order when sorting
    # by length. 
    perm = sorted(perm)
    perm = sorted(perm, key=len)
    return perm

# Testing part one
print allwords('things')
print allwords('stuff', 3)

# Part two

import random
randomWord = list()
while (len(randomWord) != 6):
    randomWord = list(''.join(random.sample(words, 1)))
random.shuffle(randomWord)
guess = ""
answers = allwords(randomWord, 4)
fourl = [word for word in answers if len(word) == 4]
fivel = [word for word in answers if len(word) == 5] 
sixl = [word for word in answers if len(word) == 6]
guessedfour, guessedfive, guessedsix = [], [], []
while (guess != 'q'):
    print "\n%s:\n" % ''.join(randomWord)
    print "%s:" % guessedfour 
    print "%d 4-letter words left." % len(fourl)
    print "%s:" % guessedfive
    print "%d 5-letter words left." % len(fivel)
    print "%s:" % guessedsix
    print "%d 6-letter words left." % len(sixl)
    guess = raw_input("\nEnter a guess: ")
    
    if guess in fourl:
        fourl = [word for word in fourl if word != guess]
        guessedfour.append(guess)
        # Could use bisect or binary/linear search rather than sorted to
        # improve efficiency, though these lists will always be small.        
        guessedfour = sorted(guessedfour) 
        print "Correct!"
    elif guess in fivel:
        fivel = [word for word in fivel if word != guess]
        guessedfive.append(guess)
        guessedfive = sorted(guessedfive)  
        print "Correct!"
    elif guess in sixl:
        sixl = [word for word in sixl if word != guess]
        guessedsix.append(guess)
        guessedsix = sorted(guessedsix)
        print "Correct!"
    elif guess != 'q': print "Incorrect."
    
    if ((len(fourl) + len(fivel) + len(sixl)) == 0):
        print "\nCongratulations! You've won."
        guess = 'q' # Could reset start rather than quitting.
    