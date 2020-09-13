import csv
import re
import collections
import gensim
import nltk
from gensim.parsing import remove_stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

slist = []
hlist = []
sDict = []
hDict = []
ps = PorterStemmer()


def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(ps.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


def word_count(lst):
    counts = dict()
    for item in lst:
        words = word_tokenize(item)

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    return counts


def writeFile(anyList, str):

        w = csv.writer(open(str, 'w'))
        for key, value in anyList.items():
            w.writerow([key, value])


with open('sms-spam-corpus.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['v1'] == 'spam':

            slist.append(stemSentence(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))

        else:

            hlist.append(stemSentence(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))

    # print(slist)
    # print(hlist)
    sDict = word_count(slist)
    hDict = word_count(hlist)
   # print(sDict)
    #print(hDict)
field_names = ['word', 'count']
writeFile(sDict,'mycsvfile.csv')
writeFile(hDict,'mycsvfile1.csv')