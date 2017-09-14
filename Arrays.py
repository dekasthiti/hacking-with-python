import cProfile, StringIO, pstats


def isUnique(inputString):
    characters = list(inputString)
    isunique = 1
    print(characters)
    total = 0
    for c in characters:
        a = ord(c) - ord('a')
        if (total & (1 << a) != 0 ): # if bit corresponding to a is set in total
            isunique = 0
            break
        else:
            total = total | (1 << a)
        print bin(total)

    if isunique:
            print("%s is unique!!" % inputString)
    else:
            print("%s is not unique!" % inputString)


def isPermutation(inputString, testString):
    isAPermutation = 0
    pr = cProfile.Profile()
    pr.enable()
    #Filter 1: Check if strings have the same length
    if len(inputString) == len(testString):
        #if list(inputString) == list(testString): #This won't work because it will compare the strings letter by letter
            #if hash(inputString) == hash(testString) # In python, strings of same length with the same letters don't hash to the same number
        if set(inputString) == set(testString):
            isAPermutation = 1
        else:
            isAPermutation = 0
    else:
        isAPermutation = 0

    pr.disable()
    s = StringIO.StringIO()
    sortBy = 'name'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortBy)
    ps.print_stats()
    print s.getvalue()
    return isAPermutation

def isPermutationSorted(inputString, testString):
    isAPermutation = 0
    pr = cProfile.Profile()
    pr.enable()
    if(len(inputString) == len(testString)):
        if(sorted(inputString) == sorted(testString)):
            isAPermutation = 1
        else:
            isAPermutation = 0
    else:
        isAPermutation = 1

    pr.disable()
    s = StringIO.StringIO()
    sortBy = 'name'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortBy)
    ps.print_stats()
    print s.getvalue()
    return isAPermutation

#1. Check if all the characters in a string are unique
isUnique("madam")
isUnique("abcs")


#2. Check if all the strings in a set are unique
# Get the binary equivalent of all strings
# xor is 0 => not unique

#3. Check if strings are permutations of each other

str1 = "madamabcdefghijklmnopqrstuvwxyz"
str2 = "abcdefghijklmnopqrstuvwxyzadamm"
isTrue = isPermutation(str1, str2)
if isTrue:
    print ("%s is a permutation of %s" %(str1, str2))
else:
    print ("%s is not a permutation of %s" %(str1, str2))

isTrue = isPermutationSorted(str1, str2)
if isTrue:
    print ("%s is a permutation of %s" %(str1, str2))
else:
    print ("%s is not a permutation of %s" %(str1, str2))


#isPermutationSorted("hello", "ello")


#To profile: 
# python -m cProfile [-o outputFile] [-s sortOrder] myFile.py
# timeit <the command>

#4. Replace all spaces in a string with %20
def replaceSpaces(inputString):
    for count, c in enumerate(inputString):
        if c == ' ':
            inputString = inputString.replace(c, '%20')
            # alternative to replace
            #inputString = inputString[:count] + '%20' + inputString[count+1:]

    return inputString 

outputStr = replaceSpaces("Mr. John Smith ")
print(outputStr)

#5. Basic string compression. Replace repeated running characters with their count
import itertools

def compressString(inputString):
    #1. replace repeat characters with count
    compressedString = ''
    inputlength = len(inputString)
    itr = enumerate(inputString)
    for count, c in itr: # this is called slicing. You can also use itertools.slice
        repetition = 0
        #while(c == list(next(itertools.islice(itr, i)))[0]):
        while count + repetition + 1 < inputlength and c == inputString[count + repetition + 1]:
            repetition = repetition + 1
            next(itertools.islice(itr, repetition-1, inputlength)) #to skip the iterator to ith place from curren
        compressedString = compressedString + c + str(repetition+1)

    #2. Check length of original and compressed string and return the shorter one
    outputStr = (inputString if inputlength < len(compressedString)  else compressedString)
    return outputStr

outputStr = compressString('aaabbcca')
print(outputStr)


# def fetch_match_and_break(inputString, inputDict)
# {
#     for count, c in list(enumerate(inputString)):
#         if c in inputDict:
#             return c;

# }

# inputDict = dict(1:'i', 2:'like', 3:'sam', 4:'sung', 5:'samsung', 6:'mobile', 7:'ice', 8:'cream', 9:'icecream', 10:'man', 11:'go', 12:'mango')
# inputString = 'ilikesamsung'

# print(fetch_match_and_break(inputString, inputDict))

# Rotate an image by 90 degrees
import numpy as np

def rotateBy90(inputMatrix):
    [rows columns] = np.shape(inputMatrix)
    left = 0
    right = columns
    down = 0
    up = rows

    # while(left < columns and down < up)
    # {
    #     tmp = inputMatrix[down, :]
    # }


inputMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print inputMatrix[0]
print np.transpose(inputMatrix)
print np.shape(inputMatrix)[1]