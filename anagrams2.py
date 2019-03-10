import sys


def find_in_dict(argv_file, argv_word):

    anagrams = []

    if len(argv_word) < 2:
        return print("INPUT ERROR: The entered word must be greater than one character")

    word_dict = read_word_list(argv_file)
    word_sorted = sortWord(argv_word)

    chars_array = list(word_sorted[0]) # Convert string to Array i.e: "abc" --> ["a","b","c"]
    all_are_equal = all(ch == chars_array[0] for ch in chars_array ) 
    
    if all_are_equal:
        return print("INPUT ERROR: Input characters must be different")

    for word in word_dict.keys():
        if (word_dict[word] == word_sorted[1] and word != word_sorted[0]):
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