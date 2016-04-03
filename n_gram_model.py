__author__ = 'mikhail'

import nltk
import operator
import csv
from nltk.tokenize import RegexpTokenizer


def top_n_gram_probability(n_count=2, dir="", top_n=10):
    d, pattern = {}, RegexpTokenizer(r'\w+')
    file = open(dir)
    raw = file.read()
    file.close()
    tokens = pattern.tokenize(raw.decode('utf-8'))
    bgs = nltk.ngrams(tokens, n_count)
    fdist = nltk.FreqDist(bgs)
    count = fdist.N()
    for k, v in fdist.items():

        if (len(k[0]) >= 2 and len(k[1]) >= 2):
            d[k] = float(v) / count

    sorted_n_grams = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_n_grams[0:top_n]

