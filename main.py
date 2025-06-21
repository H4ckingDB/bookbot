#
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
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    count = len(num_words)
    chars = count_characters(book_text)
    list = build_sorted_char_list(chars)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------") 
    for item in list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()