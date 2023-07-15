# Complete the 'getIdealNums' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER low
#  2. LONG_INTEGER high
#
# an ideal number is a positive integer with only 3 and 5 as prime factors
# it can be written as 3^i * 5^j, where i and j are non-negative integers
# find the number od ideal numbers in the range [low, high]

def getIdealNums(low, high):
    numbers = []
    
    i = 0
    j = 0
    while 3**i <= high:
        while 3**i * 5**j <= high:
            if 3**i * 5**j >= low:
                numbers.append(3**i * 5**j)
            j += 1
        i += 1
        j = 0

    return len(numbers)

# create all the permutations of a word using recursion
def permutations(word):
    if len(word) == 1:
        return [word]
    
    perms = []
    for i in range(len(word)):
        for perm in permutations(word[:i] + word[i+1:]):
            perms.append(word[i] + perm)
    return perms
    
def rearrangeWord(word):
    perms = permutations(word)
    perms.sort()
    if perms[-1] == word:
        return "no answer"
    index = perms.index(word)
    return perms[index+1]

# due to time problems i'll have to write a faster solution
def rearrangeWord(word):
    word = list(word)
    for i in range(len(word) - 1, 0, -1):
        if word[i] > word[i-1]:
            word[i], word[i-1] = word[i-1], word[i]
            return "".join(word)
    return "no answer"

# due to some errors in the test cases, i'll have to write another solution
def rearrangeWord(word):
    word = list(word)
    for i in range(len(word) - 1, 0, -1):
        if word[i] > word[i-1]:
            for j in range(len(word) - 1, i - 1, -1):
                if word[j] > word[i-1]:
                    word[i-1], word[j] = word[j], word[i-1]
                    word[i:] = word[i:][::-1]
                    return "".join(word)
    return "no answer"

print(rearrangeWord("ab"))
print(rearrangeWord("bb"))
print(rearrangeWord("hefg"))
