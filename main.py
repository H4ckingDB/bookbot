# Import system modules
import sys

# Import functions from stats.py
from stats import count_words
from stats import count_characters
from stats import build_sorted_char_list

def get_book_text(filepath):
        
    # Open the file, read the contents, and save into the
    # variable file_contents
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    count = len(num_words)
    chars = count_characters(book_text)
    list = build_sorted_char_list(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------") 
    for item in list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()