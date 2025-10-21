from stats import *
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        # Store our books as a string
        file_path = sys.argv[1]
        book = get_book_text(file_path)

        num_words = count_words(book)
        character_count = count_char(book)
        characters = sort_char(character_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("-------- Character Count --------")
        for i in range(len(characters)):
            print(f"{characters[i]["char"]}: {characters[i]["num"]}")
        print("============== END =============")

main()