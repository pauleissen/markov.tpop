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

Along with markov-tpop.py are several text files, including ones that
demonstrate that (thanks to K&P) markov-tpop.py does NOT require any
edge-case code to handle empty text files and files that contain only
one or two words.

Copyright (c) 2018 by Paul Eissen. This work is made available under
a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

![Creative Commons Attribution-ShareAlike button](https://licensebuttons.net/l/by-sa/4.0/88x31.png)
