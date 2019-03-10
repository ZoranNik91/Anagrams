import sys


def find_in_dict(L, w):

    anagrams = []

    word_dict = read_word_list(L)
    word_sorted = sortWord(w)
        
    for word in word_dict.keys():
        if (word_dict[word] == word_sorted[1]):
            anagrams.append(word)
       
    print(len(anagrams))


def sortWord(input_word): 
    """Lowercase and sort the user input word."""
    word = input_word.lower().strip()
    return word, "".join(sorted(word)) # "".join Array to empty String


def read_word_list(filename):
    """Open file and create a dictionary of {"word":"word_sorted"}."""
    with open(filename, "r") as word_file:
        word_list = {}
        for text in word_file:
            word_sorted = sortWord(text)
            word_list.update({word_sorted[0]: word_sorted[1]}) # inserts property : value into word_list dictionary
        return word_list


def main():
    if len(sys.argv) != 3:
        return print("INPUT ERROR: Use like: anagram.py fileName.txt word")
    find_in_dict(sys.argv[1], sys.argv[2])

if __name__ == "__main__": # the test1.py is __main__ only when run directly from terminal.
    exit(main())