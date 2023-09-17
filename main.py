

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    #Create an empty dictionary
    letter_count = {}
    """count character occurences
    if letter is an alphabet add to dictionary and count"""
    for letter in text:
        #convert string into lower case and then split by characters using Python's list function
        lowered = letter.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    #sort dictionary by highest occuring value first. items() will give both keys and values and we use values to sort with lambda function
    return letter_count

def chars_dict_to_sorted_list(char_dict):
        return dict(sorted(char_dict.items(), key=lambda x:x[1], reverse=True))


def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = count_words(text)
    num_letters = count_letters(text)
    char_sorted_dict = chars_dict_to_sorted_list(num_letters)

    print(f"--- Begin report of {path_to_file} --- \n")
    print(f"{num_words} words found in the document \n")
    print()
    for letter in char_sorted_dict:
        if letter.isalpha():
            print(f"the '{letter}' character was found {char_sorted_dict[letter]} times")
    print("--- End report ---")

main()
