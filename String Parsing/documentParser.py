with open("Strings.txt","r") as f: text = file.read(f)
text = text.lower()
charList = list(text)

exclude = '''!"#$%&()*+,-./:;<=>?@[\]^_`{|}~1234567890'''
space = ' '
charList = [value if value not in exclude else space for value in charList]
        
text = ''.join(charList) # Convert back to string

words = dict()
for word in text.split(): words[word] = words.get(word, 0) + 1

from operator import itemgetter
sortedWords = sorted(words.items(), key=itemgetter(1), reverse=True)

wordLength = max(len(word) for word in words.keys())
valueLength = max(len(str(value)) for value in words.values())
    
for word, occurrences in sortedWords:
    print ("%*s: %*d" % (wordLength, word, valueLength, occurrences))
