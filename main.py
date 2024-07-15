import random

# This program creates a predictive text model using n-gram analysis to suggest
# words to follow a given reference word
depth = 2

referenceText = "sources/beemovie.txt"
textFile = open(referenceText)
words = textFile.read().split()

window = []
freqDict = {}

#Create frequency dictionary
for word in words:
    cleanWord = word.strip('.;,-“’”:?—‘!()_').lower()
    if len(cleanWord) != 0:
        window.append(cleanWord)
        if len(window) > depth + 1:
            window.pop(0)
        if len(window) > depth:
            key = tuple(window[0:-1])
            val = window[len(window)-1]

            if key not in freqDict:
                freqDict[key] = [val]
            else:
                freqDict[key].append(val)

current = ("and","then")
for i in range(10):
    print(current[0])
    current = (current[1],random.choice(freqDict[current]))