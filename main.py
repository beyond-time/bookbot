import sys

from stats import get_num_words
from stats import get_char_count
from stats import sort_chars

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        words = get_num_words(file_contents)
        # print(f"{words} words found in the document")
        chars = sort_chars(get_char_count(file_contents))
    
    # print(chars)
    return words, chars

def main():
    print(len(sys.argv))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    #"books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    words, chars = get_book_text(path)
    # print(chars)
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    

main()
