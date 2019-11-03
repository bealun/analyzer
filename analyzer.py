#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Text analyzer functions
"""
filename = "phil.txt"



def line_counter():
    """
    Counting number of lines in textfile
    """
    number_lines = 0
    with open(filename, "r") as file:
        for line in file:

            if not line.strip():
                continue

            number_lines += 1

    file.close()
    return number_lines



def word_counter():
    """
    Counting number of words in textfile
    """
    wordcount = 0
    with open(filename, "r") as file:
        for line in file:
            wordcount += len(line.split())

    file.close()
    return wordcount



def letter_counter():
    """
    Counting amount of letters in textfile
    """
    file = open(filename, "r")
    text = file.read().replace("\n", "").replace(".", "").replace(",", "").replace(" ", "").replace("-", "")
    lettercount = len(text)

    file.close()
    return lettercount



def word_frequency():
    """
    7 most used words in textfile
    """
    return_string = ""
    file = open(filename, "r")
    contents = file.read()
    words = contents.split()
    word_count = word_counter()

    for i, _ in enumerate(words):
        words[i] = words[i].lower()
        words[i] = words[i].strip(',:.;')
    counter = dict()

    for i, _ in enumerate(words):
        if words[i] not in counter:
            counter[words[i]] = 1
        else:
            counter[words[i]] += 1
    sorted_words = list(sorted(counter, key=counter.get, reverse=True))

    for w in sorted_words[0:7]:

        return_string += "'" + w + "'" + ' used: ' + str(counter[w])
        return_string += ' : ' + str(round(counter[w] / word_count * 100, 1)) + "% \n"
    file.close()
    return return_string



def letter_frequency():
    """
    7 most used letters in textfile
    """
    file = open(filename, "r")
    charcount = {}
    validchars = "abcdefghijklmnopqrstuvwxyz"
    return_string = ""
    letter_count = letter_counter()

    for i in range(97, 123):
        c = (chr(i))
        charcount[c] = 0

    for line in file:
        words = line.split(" ")
        for word in words:
            chars = list(word)

            for c in chars:
                if c.isalpha():
                    if c.isupper():
                        c = c.lower()
                    if c in validchars:
                        charcount[c] += 1

    sorted_letters = list(sorted(charcount.items(), key=lambda charcount: charcount[1], reverse=True))

    for key, value in sorted_letters[0:7]:
        return_string += "'" + key + "'" + ' used: ' + str(value)
        return_string += ' times: ' + str(round(value / letter_count * 100, 1)) +"% \n"
    file.close()
    return return_string




def analyze_all():
    """
    Showing results from every menu choice
    """
    print("lines: ", line_counter(), "\n")
    print("words: ", word_counter(), "\n")
    print("letters: ", letter_counter(), "\n")
    print("word frequency: \n" + word_frequency(), "\n")
    print("letter frequency: \n" + letter_frequency(), "\n")
