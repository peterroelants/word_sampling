# File to contains the alias method class that is able to generate samples
# from a discrete distribution in constant time.
# More info on the alias method: http://www.keithschwarz.com/darts-dice-coins/

import random


class AliasMethod(object):
    """
    Class that is able to generate samples from a discrete distribution in constant time.
    Based upon Vose's Alias Method described at: http://keithschwarz.com/darts-dice-coins/

    Initialisation is linear with respect to the size of the vocabulary.
    Sample generation is constant.
    Memory usage is linear with respect to the size of the vocubulary.
    """
    def __init__(self, word_frequencies):
        """
        Initialise the alias method mappings.
        Set the alias and probability tables needed to generate samples.

        :param word_frequencies:
            list of (word, frequency) tuples
        """
        # Calculate the total number of words in the text (sum of all occurences)
        total_wordcount = float(sum([t[1] for t in word_frequencies]))
        # Get the size of the vocabulary
        self.vocab_size = len(word_frequencies)
        # Create a list with (word, normalized probability) elements.
        # normalized probabilities = p_i * vocab_size
        self.words = [(key, (count * self.vocab_size) / total_wordcount)
                      for key, count in word_frequencies]
        # Create the alias and probability tables
        # The alias table will hold the alternative to chose
        self.alias = [None for _ in xrange(self.vocab_size)]
        # The probability table will hold the probability of picking the native
        #  word instead of the alias
        self.prob = [None for _ in xrange(self.vocab_size)]
        # Create the small and large worklists
        # small contains the words with a normalized probability < 1
        small = []
        # large contains the words with a normalized probability >= 1
        large = []
        # fill the small and large lists with the words and their probabilities
        for idx, (key, np) in enumerate(self.words):
            if np < 1:
                small.append((idx, np))
            else:  # np >= 1
                large.append((idx, np))
        # Start computing the probability and alias tables
        while small and large:  # while small and large are not empty
            # remove a large and small element to fill a prob and alias column
            l_idx, l_np = small.pop()
            g_idx, g_np = large.pop()
            # fill a prob and alias column
            self.prob[l_idx] = l_np
            self.alias[l_idx] = g_idx
            # update g_np and add (g_idx, g_np) back to the correct list
            g_np = (g_np + l_np) - 1
            if g_np < 1:
                small.append((g_idx, g_np))
            else:  # g_np >= 1
                large.append((g_idx, g_np))
        for g_idx, g_np in large:  # iterate over remaining large elements
            # Remaining element should have probability 1
            self.prob[g_idx] = 1
        for l_idx, l_np in small:  # iterate over remaining small elements
             # Remaining element should have probability 1
            self.prob[l_idx] = 1

    def sample(self):
        """
        Sample from the discrete distribution represented by this alias method table.

        :return:
            A word sampled from the distribution.
        """
        # Generate a fair die roll to select the column
        column = random.randrange(self.vocab_size)
        # Flip a biased coin to select the word at the current column of the alias
        # Select the element or alias
        if random.random() >= self.prob[column]:
            column = self.alias[column]
        return self.words[column][0]