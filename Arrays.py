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
    [rows, columns] = np.shape(inputMatrix)
    left = 0
    right = columns - 1 # 0 based indexing
    down = 0
    up = rows - 1 # 0 based indexing
    outputMatrix = np.ones((rows, columns))

    while (left < right and down < up):
        for i, j in zip(range(rows), range(columns)): #https://stackoverflow.com/questions/18648626/for-loop-with-two-variables
            #outputMatrix[first_row][j from first_column to last_column)] = inputMatrix[i from last_row to first_row][first_column] # there is a double copy here for elements in the corner    
            outputMatrix[down][j] = inputMatrix[up-i][left]
            #outputMatrix[down][:] = inputMatrix[-up:][left] (#check if you can use slice indices)


        for i, j in zip(range(rows), range(columns)):   
            #outputMatrix[i in first_row + 1 (to account for corner element) to last_row][last_column] = inputMatrix[first_row][j from first_column to last_column]
            outputMatrix[i][right] = inputMatrix[down][j]


        for i, j in zip(range(rows), range(columns)):
            #outputMatrix[last_row][j in last_column + 1 (to account for corner element) to first_column] = inputMatrix[i in first_row + 1 to last_row][last_column]
            outputMatrix[up][right-j] = inputMatrix[i][right]


        for i, j in zip(range(rows), range(columns)):
            #outputMatrix[i in last_row + 1 to first_row][first_column] = inputMatrix[last_row][j in last_column+1 to first_column]
            outputMatrix[up - i][left] = inputMatrix[up][right - j]
            

        ##1st input row done: move down one step toward up
        down+=1

        #1st input column done: move left one step toward the right
        left+=1

        #last input column done: move right one step toward left
        right-=1

        #last input row donw: move up one step toward down
        up-=1

    #Center element (when left = right = up = down)
    outputMatrix[down][left] = inputMatrix[up][right]

    return outputMatrix

inputMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print inputMatrix
#print np.transpose(inputMatrix)
#print np.shape(inputMatrix)[1]
outputMatrix = rotateBy90(inputMatrix) # what are the dots in the printed output?!!
print outputMatrix

#@CTCI 7: If an element in a matrix is 0, force all elements in the entire row
# and column intersecting this element to be 0
import numpy as np
def zeroOutRowCol(inputMatrix):
    #Get the [x, y] position of this element
    # lists allow retrieving index like this: tmplist.index(value you are looking for)
    # testlist.index(element) if element in testlist else None
    # or, for i in [i for i,x in enumerate(testlist) if x == 1]:
    # np arange / arrays don't have the option
    # Set [x, :] and [:, y] to 0
    #inputMatrix[:, 1] = inputMatrix[1,:] = [0,0,0]  #this notation works only for numpy arrays
    
    [rows, columns] = np.shape(inputMatrix)
    #outputMatrix =  inputMatrix  # this makes output an alias of input, changing input when output changes
    outputMatrix = np.zeros((rows, columns))
    #for i in rows:  #int object not iterable error!
    #    for j in columns: # int object not iterable error!
    outputMatrix[:,:] = inputMatrix[:,:]
    for i in range(rows):
         for j in range(columns):
            if inputMatrix[i][j] == 0:
                outputMatrix[i, :] = outputMatrix[:, j] = 0

    return outputMatrix

inputMatrix = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
outputMatrix = zeroOutRowCol(inputMatrix)
print outputMatrix

# @CTCI8. Detect if a string is a rotated version of an another string.
# This will fail when the test string is shorter than the original, for eg: dentstu and dentst
# will both be detected as rotated versions of the original. Add size check
def isRotated(originalString, testString):

    #check if the size of both the strings are the same.
    if len(originalString) == len(testString):
        #append the originalString to itself
        appendedString = originalString + originalString

        #look for the rotatedString in the appendedString. Do substring search
        #if found, testString is a rotated version of original string
        if testString in appendedString:
            return True
        else:
            return False
    else:
        return False

originalString = 'student'
testString = 'dentst'
print(isRotated(originalString, testString))

# Reverse a string in a way that "I am a test string" becomes "string test a am I"
def reverse(inputString):
    # There is no reverse() function for str. Rationale is in "https://stackoverflow.com/questions/931092/reverse-a-string-in-python"
    # Using slicing instead
    # From end to beginning in steps of -1
    tmp = inputString[-1::-1] 
    #tmp2 = []
    tmp2 = '' # this is a string object. Declaring and initializing tmp2 = [] makes it a list and
              # you can call append on it. You cannot call append on a string object
    for s in tmp.split(' '):
        # since strings are immutable, when you concatenate, you 
        # create a new string, can be very expensive, though CPython 
        # has a way to optimize this
        # Recommendation is to use append instead, but append adds 
        # array of words to the list, like ['string', 'test', 'a', 'am', 'I']
        #tmp2.append(s[-1::-1] + ' ')
        tmp2+= s[-1::-1] + ' '
    return tmp2

inputString = "I am a test string"
outputString = reverse(inputString)
print("Reverse string is: %s" % outputString)
