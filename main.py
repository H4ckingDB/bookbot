#
from stats import count_words
from stats import count_characters

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
    count_characters(book_text)
    print(f"{count} words found in the document")

main()