import sys
import time

timeStart = time.time()

def sort_word(word): 
    """Converts a string to sorted lowercase string: 'Zba' -> 'abz'"""
    return "".join(sorted(word.strip().lower()))


def has_all_same_characters(word):
    """Returns boolean, True if all lowercased characters in word are equal: 'bBb' -> True"""
    arr = list(word.lower())
    return all(ch == arr[0] for ch in arr)


def create_anagram(filename, word):
    """Read file line by line and detect if word is anagram of input word"""
    anagrams = []
    word_sorted = sort_word(word)
    word_len = len(word_sorted)
    ch0 = word_sorted[0]
    with open(filename, "r") as word_file:
        for file_line in word_file:
            line_sorted = sort_word(file_line)
            if (ch0 == line_sorted[0] and word_len == len(line_sorted) and word_sorted == line_sorted):
                anagrams.append(file_line.strip())

    return "Found: " + str(len(anagrams)) +  "\nTime: " + str(time.time() - timeStart)


def main():
    if len(sys.argv) != 3:
        return print("ERROR: Missing arguments\nUse like: anagram.py fileName.txt word")
    if len(sys.argv[2]) < 2:
        return print("ERROR: Invalid word length\nThe entered word must be at least two characters long")
    if has_all_same_characters(sys.argv[2]):
        return print("ERROR: Word characters must be different")
    return create_anagram(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    exit(main())