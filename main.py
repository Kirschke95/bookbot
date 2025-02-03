def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = count_words(text)
    #print(word_count)

    character_counts_dict = count_characters(text)
    #print(character_counts)

    character_counts_list = dict_to_list(character_counts_dict)
    character_counts_list.sort(reverse=True, key=sort_on)
    print_report(character_counts_list, book_path, word_count)

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    num = 0
    for word in words:
        num += 1
    return num

def count_characters(text):
    text = text.lower()
    character_counts = {}

    for char in text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts

def dict_to_list(char_dict):
    char_list = []

    #loop through dictionary items
    for char, count in char_dict.items():
        #create dictionary for this character and add it to the list
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)

    return char_list

def print_report(characters, path, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    for character in characters:
        if character["char"].isalpha():
            print(f"The '{character["char"]}' was found {character["num"]} times.")
        
    print("--- End report ---")

    



main()