#!/usr/bin/env python
#
# Python 2.x implementation of the Markov chain algorithm as described
# in Kernighan and Pike, "The Practice of Programming" (Addison-Wesley,
# 1999), Chapter 3, pp. 61-75.
#
# Suggested usage:
#     ./markov-tpop.py < TEXTFILE | fmt | more
# where TEXTFILE contains English prose.
#
# Copyright (c) 2018 by Paul Eissen. This work is made available
# under a Creative Commons Attribution-ShareAlike 4.0 International
# License. https://creativecommons.org/licenses/by-sa/4.0/

import sys
import random
import string

NPREF = 2
NONWORD = '\n'

# Each record consists of a tuple(prefix) key and suffix list data.
statetab = {}

def generate(nwords):
    """
    Print up to nwords or stop when a NONWORD suffix is encountered,
    whichever comes first.
    """
    prefix = []

    # The first prefix in statetab consists of two NONWORDs.
    for i in range(NPREF):
        prefix.append(NONWORD)

    random.seed()

    for i in range(nwords):
        suffixes = statetab[tuple(prefix)]
        word = random.choice(suffixes)
        if word == NONWORD:
            break
        print word,
        prefix.pop(0)
        prefix.append(word)

    return

def add(prefix, word):
    """
    prefix is a list and word is a string.
    """

    key = tuple(prefix)
    if key in statetab:
        statetab[key].append(word)
    else:
        statetab[key] = [word]
    return

def build(prefix):
    """
    prefix is an INOUT list.
    """

    for line in sys.stdin.readlines():
        if len(line.strip(string.whitespace)) == 0:
            continue
        for word in line.split():
            add(prefix, word)
            prefix.pop(0)
            prefix.append(word)

    return

if __name__ == '__main__':
    """
    prefix is assigned two NONWORDs, so that when build() and add() complete
    their work, statetab will look like this ("IW" means "input word" and N
    represents the number of input words):

        prefix#        prefix          suffix(es)
        -------------------------------------------------
           1      NONWORD, NONWORD      1st IW
           2      NONWORD, 1st IW       2nd IW
           3      1st IW, 2nd IW        ...
          ...
          last    N-1 IW, N IW          NONWORD

    generate() will automagically print the first two input words.
    """

    MAXGEN = 10000

    prefix = []

    for i in range(NPREF):
        prefix.append(NONWORD)

    build(prefix)
    add(prefix, NONWORD)

    generate(MAXGEN)

    sys.exit(0)
