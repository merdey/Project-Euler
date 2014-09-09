"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def nameScore(name):
    nameScore = 0
    name = name[1:-1] #trim "" from names
    for letter in name:
        nameScore += ( ord(letter) - 64 )
    return nameScore

namesFile = open('p022_names.txt')
namesList = namesFile.read().split(',')
namesFile.close()

namesList.sort()
namesSum = 0
i = 1
for name in namesList:
    namesSum += ( nameScore(name) * i )
    i += 1
print(namesSum)
    
