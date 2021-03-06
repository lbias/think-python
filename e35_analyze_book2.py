from __future__ import print_function, division
from e34_analyze_book1 import process_file

def subtract(d1, d2):
    """Returns a set of all keys that appear in d1 but not d2.
    d1, d2: dictionaries
    """
    return set(d1) - set(d2)

def main():
    hist = process_file('emma.txt', skip_header=True)
    words = process_file('words.txt', skip_header=False)

    diff = subtract(hist, words)
    print("The words in the book that aren't in the word list are:")
    for word in diff:
        print(word, end=' ')

if __name__ == '__main__':
    main()
