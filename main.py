from stats import sort_dictionaries, word_count
from stats import number_of_characters
import sys

args = sys.argv
args[0] = "main.py"
if len(args) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path_file):
    with open(path_file) as f:
        file_content = f.read()
    return file_content


def main():
    text = get_book_text(args[1])
    count = word_count(text)
    characters = number_of_characters(text)
    sorted_dict = sort_dictionaries(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_dict:
        a = char_dict["char"]
        if a.isalpha():
            print(f"{a}: {char_dict['num']}")


main()
