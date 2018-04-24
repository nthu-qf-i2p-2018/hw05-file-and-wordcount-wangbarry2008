# -*- coding: utf-8 -*-
import string
from collections import Counter
import csv
import json
import pickle


def main(filename):
    # read file into lines
    lines = open(filename).readlines()

    # declare a word list
    all_words = []

    # extract all words from lines
    for line in lines:
        # split a line of text into a list words
        # "I have a dream." => ["I", "have", "a", "dream."]
        words = line.split()
        # check the format of words and append it to "all_words" list
        for word in words:
            # then, remove (strip) unwanted punctuations from every word
            # "dream." => "dream"
            word = word.strip(string.punctuation)
            # check if word is not empty
            if len(word) != 0:
                # append the word to "all_words" list
                all_words.append(word)

    # compute word count from all_words
    counter = Counter(all_words)
    wordcomputer = counter.most_common()

    # dump to a csv file named "wordcount.csv":
    # word,count
    # a,12345
    # I,23456
    # ...
    with open('wordcount.csv', 'w') as csv_file:
        # create a csv writer from a file object (or descriptor)
        writer = csv.writer(csv_file, lineterminator='\n')
        # write table head
        writer.writerow(['word', 'count'])
        # write all (word, count) pair into the csv writer
        writer.writerows(wordcomputer)

    # dump to a json file named "wordcount.json"
    json.dump(wordcomputer, open('wordcount.json', 'w'))

    # BONUS: dump to a pickle file named "wordcount.pkl"
    # hint: dump the Counter object directly
    pickle.dump(wordcomputer, open('wordcount.pkl', 'wb'))


if __name__ == '__main__':
    main("i_have_a_dream.txt")
