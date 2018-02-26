## Markov Chain Algorithm in Python

This is my Python 2.x implementation of the Markov chain algorithm
described in Kernighan and Pike's [The Practice of Programming](https://www.cs.princeton.edu/~bwk/tpop.webpage/)
(Reading, MA: Addison-Wesley, 1999), Chapter 3, pp. 61-75.

Usage:
```
    ./markov-tpop.py < TEXTFILE | fmt
    cat TEXTFILE | ./markov-tpop.py | fmt
```
where TEXTFILE is the name of a file containing English text.

`markov-tpop.py` comes with several text files to play with, including some
that show (thanks to K&P) how the script avoids the use of edge-case code
to handle empty text files, files with one word, and files with two words.

Copyright (c) 2018 by Paul Eissen. This work is made available under
a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

[[[https://licensebuttons.net/l/by-sa/4.0/88x31.png]]](https://creativecommons.org/licenses/by-sa/4.0/)
