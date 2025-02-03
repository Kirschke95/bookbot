def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count = count_words(text)
    #print(word_count)

    character_counts = count_characters(text)
    #print(character_counts)

    print_report(character_counts, book_path, word_count)

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

def print_report(characters, path, word_count):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    for character in characters:
        print(f"The '{character}' was found {characters[character]} times.")

    



main()