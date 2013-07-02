filename = input('Enter a file name: ')

longestPalindrome = ''

with open(filename) as f:
    fstring = f.read()
    
escapeCharacters = ["\n", "\r"]
for char in escapeCharacters:
    fstring = fstring.replace(char, "")

length = len(fstring)
    
for i in range(0, length+1):
    for j in range(0, length+1):
        contender = fstring[i:j]
        reversedContender = contender[::-1]
        if contender == reversedContender and j-i > len(longestPalindrome):
            longestPalindrome = contender
                
print('The longest palindrome is:', longestPalindrome)