import re, string
from collections import Counter
file = open('a-tale-of-two-cities.txt', 'r')
# text = file.read().lower()
short = 'a , very , short . example ; to - test ` punctuation'
long = '''
From an efficiency perspective, you're not going to beat

s.translate(None, string.punctuation)
It's performing raw string operations in C with a lookup table - there's not much that will beat that but writing your own C code.

If speed isn't a worry, another option though is:

exclude = set(string.punctuation)
s = ''.join(ch for ch in s if ch not in exclude)
This is faster than s.replace with each char, but won't perform as well as non-pure python approaches such as regexes or string.translate, as you can see from the below timings. For this type of problem, doing it at as low a level as possible pays off.

Timing code:

import re, string, timeit

s = "string. With. Punctuation"
exclude = set(string.punctuation)
table = string.maketrans("","")
regex = re.compile('[%s]' % re.escape(string.punctuation))

def test_set(s):
    return ''.join(ch for ch in s if ch not in exclude)

def test_re(s):  # From Vinko's solution, with fix.
    return regex.sub('', s)

def test_trans(s):
'''

def getListOfWords(text):
    list = text.translate(string.maketrans("", ""), string.punctuation)
    return re.split('\s+', list)

def getTotalNumberOfWords(list):
    return len(list)

''' returns the number of UNIQUE words in the novel. '''
def getTotalUniqueWords(list):
    cnt = Counter()
    for word in list:
        cnt[word] += 1
    return cnt

''' return the 20 most frequently used words in the novel and the number of times they were used '''
def get20MostFrequentWords(list):
    return list.most_common(20)

''' filters the most common 100 English words and then returns the 20 most
 frequently used words and the number of times they were used '''
def get20MostInterestingFrequentWords():
    pass

''' returns the 20 LEAST frequently used words and the number of times they were used '''
def get20LeastFrequentWords(list):
    return list[:-21:-1]

def getFrequencyOfWord(text):
    text.split("Chapter [0-9]+\n")

def getChapterQuoteAppears(list):
    pass

def generateSentence(list):
    pass

list = getListOfWords(short)
num = getTotalNumberOfWords(list)
total = getTotalUniqueWords(list)
mostCommon20 = get20MostFrequentWords(total)
leastCommon20 = get20LeastFrequentWords(mostCommon20)

print '\nList of words: \n'
print list
print '\nTotal number of words: \n'
print num
print '\nTotal unique words: \n'
print total
print '\n20 Most common words: \n'
print mostCommon20
print '\n20 Least common words: \n'
print leastCommon20
