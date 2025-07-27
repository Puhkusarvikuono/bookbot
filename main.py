import sys
from stats import get_num_words, get_character_count, dictionary_sorter

if len(sys.argv) == 2:
    book_path = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
#    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_character_count(text)
    sorted_count = dictionary_sorter(char_count)
    for item in sorted_count:
        print(f"{item['name']}: {item['num']}")
    print("============= END ===============")



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
