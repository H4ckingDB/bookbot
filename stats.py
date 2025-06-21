def count_words(book_text):
    words = book_text.split()
    return words

def count_characters(text):
    dictionary = {'a': 0, 'b': 0, 'c': 0,
    'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0,
    'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
    'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
    's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0,
    'x': 0, 'y': 0, 'z': 0
    }

    for char in text:
        char = char.lower()
        #print(char)
        if char in dictionary:
            dictionary[char] += 1
    return dictionary

def sort_on(items):
    return items["num"]

def build_sorted_char_list(char_dict):
    sorted_chars = []
    for char, num in char_dict.items():
        if char.isalpha():
            temp_dict = {"char": char, "num": num}
            sorted_chars.append(temp_dict)
    sorted_chars.sort(reverse=True, key=sort_on)
    #print(sorted_chars)
    return sorted_chars
    