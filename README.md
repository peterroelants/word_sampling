# Sample from a distribution of words

Code to read a corpus from a file, and sample `n` words from the word occurrence distribution of that file. The file `main.py` takes two arguments: a path to a corpus and an integer specifying how many samples are desired. For example run:

    python main.py ./data/pg11.txt 10

To generate 10 samples from the word distribution defined by the corpus at `./data/pg11.txt`.

## Parsing the corpus

Only standard libraries are used. The lines in the corpus are split into tokens with a very simple regular expression. More advanced tokenisation can be achieved with the help of the [NLTK library](http://www.nltk.org/). Lines are converted to lowercase during tokenisation.

During parsing, a Python dictionary is used to hold the current number of occurrences of each token. 


## Alias sampling method

The [alias method](http://en.wikipedia.org/wiki/Alias_method) is used to create a data-structure that allows for efficient sampling from the word occurrence distribution. The algorithm can sample from the distribution in O(1) constant time. The memory usage is O(n), and the preprocessing uses O(n) time.

The alias method implemented here is based upon the description by [Keith Schwarz](http://keithschwarz.com/darts-dice-coins/).