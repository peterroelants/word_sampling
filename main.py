#! /usr/bin/env python

# Main file to be executed from the command line

import sys
import re
from alias_method import AliasMethod


def initialize_sampler(file_path):
    """
    Load the corpus in the given file_path, count al the words,
    and create a sampler to sample the words from the distribution of
    word occurences in the corpus.

    :param file_path:
        File path name string where the corpus to be loaded can be found

    :return
        An alias method sampler to sample random words
    """
    # Define a regex to split the input into word tokens
    word_tokenize_regex = r'(\w+)'
    regex_pattern = re.compile(word_tokenize_regex)
    # Define the dictionary that is used to count the words
    count_dict = dict()
    # Open the file and read line by line
    with open(file_path) as f:
        for line in f:
            # Extract all words in the current line
            result = regex_pattern.findall(line.lower())
            # Update the count dictionary
            for word in result:
                if word in count_dict:
                    count_dict[word] += 1
                else:
                    count_dict[word] = 1
    # Extract all the (word, count) tuples and pass them to the AliasMethod constructor
    items = count_dict.items()
    return AliasMethod(items)


def get_n_samples(random_word_sampler, n):
    """
    Generate n samples from the given word sampler.

    :param random_word_sampler
        A AliasMethod instance that can sample from the distribution
    :param n
        The number of words to generate

    :return
        A generator that generates n samples drawn from the random_word_sampler distribution.
    """
    for i in xrange(n):
        yield random_word_sampler.sample()


def main():
    """
    Main function to be run
    """
    # get the arguments
    file_path = sys.argv[1]
    nb_of_samples = int(sys.argv[2])
    # Create the sampler
    random_word_sampler = initialize_sampler(file_path)
    # Sample ant print the words
    for sample in get_n_samples(random_word_sampler, nb_of_samples):
        print sample


if __name__ == "__main__":
    main()