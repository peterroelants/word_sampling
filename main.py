#! /usr/bin/env python

# Main file to be executed from the command line
from alias_method import AliasMethod


def initialize_generator():
    ls = [('a', 1.0/8), ('b', 1.0/5), ('c', 1.0/10), ('d', 1.0/4), ('e', 1.0/10), ('f', 1.0/10), ('g', 1.0/8)]
    return AliasMethod(ls)


def get_n_samples(generator, n):
    for i in xrange(n):
        yield generator.sample()


def main():
    """
    Main function to be run
    """
    generator = initialize_generator()
    d = dict()
    for sample in get_n_samples(generator, 1000000):
        if sample in d:
            d[sample] += 1
        else:
            d[sample] = 1

    items = d.items()
    items = [(key, count / 1000000.0) for key, count in items]
    print items






if __name__ == "__main__":
    main()