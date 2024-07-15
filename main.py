import random

# This program creates a predictive text model using n-gram analysis to suggest
# words to follow a given reference word
depth = 3

shrek = open("sources/shrek1.txt").read().split()

dict = {}

def analyze(freqDict, words):
    window = []
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

analyze(dict, shrek)

current = ("i'm","going","to")
for i in range(20):
    print(current[0],end=" ")
    current = (current[1],current[2],random.choice(dict[current]))