import re, string, sys, random
from itertools import islice
from collections import Counter
from trie import Trie
file = open('a-tale-of-two-cities.txt', 'r')
text = file.read()

def getListOfWords(text):
    word_list = text.translate(string.maketrans("", ""), string.punctuation)
    return re.findall('\w+', word_list)

def getTotalNumberOfWords(word_list):
    return len(word_list)

''' returns the number of UNIQUE words in the novel. '''
def getTotalUniqueWords(word_list):
    cnt = Counter()
    for word in word_list:
        cnt[word] += 1
    return cnt

''' return the 20 most frequently used words in the novel and the number of times they were used '''
def get20MostFrequentWords(word_list):
    return Counter(word_list).most_common(20)

''' returns the 20 LEAST frequently used words and the number of times they were used '''
def get20LeastFrequentWords(word_list):
    return Counter(word_list).most_common()[:-21:-1]

''' filters the most common 100 English words and then returns the 20 most
 frequently used words and the number of times they were used '''
def get20MostInterestingFrequentWords(word_list):
    file = open('most-common-words.txt')
    common_word = re.findall('\w+', file.read().lower())
    common_word = common_word[:100]

    mostInteresting = []
    mostCommon120 = Counter(word_list).most_common(120)
    for (word, cnt) in mostCommon120:
        if word not in common_word:
            mostInteresting.append((word, cnt))

    return mostInteresting[:20]

''' Get headings and text of chapters
Got the code idea from https://github.com/JonathanReeve/chapterize/blob/master/chapterize/chapterize.py
'''
def getChapters(text):
    lines = text.split('\n')
    romanNumerals = '(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'
    enumerators = romanNumerals
    separators = '(\. | )'
    titleCase = '[A-Z][a-z]'

    pat = re.compile(enumerators + separators + titleCase)

    headings = []
    headlines = []
    for i, line in enumerate(lines):
        if pat.match(line) is not None:
            # heading = line.split(' ', 1)
            # headings[heading[0]] = heading[1]
            headings.append(line)
            headlines.append(i)

    chapters = []
    lastHeadline = len(headlines) - 1
    for i, headline in enumerate(headlines):
        if i is not lastHeadline:
            nextHeadline = headlines[i+1]
            chapters.append(lines[headline+1:nextHeadline])

    return headings, chapters

def getFrequencyOfWord(word, chapters):
    freq = []
    for chapter in chapters:
        cnt = 0
        for line in chapter:
            cnt = cnt + line.count(word)
        freq.append(cnt)
    return freq

def getChapterQuoteAppears(quote, headings, chapters):
    for i, chapter in enumerate(chapters):
        for line in chapter:
            if quote in line:
                return i+1
    return -1

def generateSentence(word_list):
    get_indexes = lambda word, word_list: [i for (item, i) in zip(word_list, range(len(word_list))) if word == item]
    sentence = 'the'
    index = random.choice(get_indexes(sentence, word_list))

    for i in range(10):
        index = index + 1
        next = word_list[index]
        sentence = sentence + ' ' + word_list[index]
        index = random.choice(get_indexes(next, word_list))

    return sentence

def getAutocompleteSentence(uniques, start):
    trie = Trie()
    for word in uniques:
        trie.insert(word)
    return trie.autocomplete(start)

word_list = getListOfWords(text)
num = getTotalNumberOfWords(word_list)
uniques = getTotalUniqueWords(word_list)
mostCommon20 = get20MostFrequentWords(word_list)
interesting20 = get20MostInterestingFrequentWords(word_list)
leastCommon20 = get20LeastFrequentWords(word_list)
headings, chapters = getChapters(text)
frequency = getFrequencyOfWord('Bastille', chapters)
chapterQuote = getChapterQuoteAppears('it was the spring of hope', headings, chapters);
sentences = getAutocompleteSentence(uniques, 'France')
sentence = generateSentence(word_list)

# print '\nList of words: \n', word_list
# print '\nTotal number of words: \n', num
# print '\nTotal unique words: \n', len(uniques)
# print '\n20 Most common words: \n'
# print mostCommon20
# for i, (word, cnt) in enumerate(mostCommon20):
#     print word, cnt
# print '\n20 Least common words: \n', leastCommon20
# for (word, cnt) in leastCommon20:
#         print word, cnt
# print '\n20 Most interesting frequent words\n', interesting20
# for (word, cnt) in interesting20: print word, cnt
# print '\nFrequencies of words in chapters: \n', frequency
# print '\nQuote belongs to chapter', chapterQuote
# print '\nAutocomplete Sentences:', sentences
print '\nGenerate sentence:', sentence
