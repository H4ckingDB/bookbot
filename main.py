def get_book_text(filepath):
        
    # Open the file, read the contents, and save into the
    # variable file_contents
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_text)
    count = len(num_words)
    print(f"{count} words found in the document")

main()