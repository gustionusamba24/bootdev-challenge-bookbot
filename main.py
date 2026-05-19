import sys
from stats import get_num_words, get_num_chars, sort_chars_list

"""
    fn => get_book_content:
        Reads the contents of a file and return it as a string.
"""
def get_book_content(filepath: str) -> str:
    with open(filepath) as f:
        book_contents = f.read()

        return book_contents

"""
    fn => main:
        The entry point of the program.
"""
def main():
    # Make sure there are two arguments given
    # Check if the user provided the path to the book as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Take the relative path of the book
    # The first argument (index 0) is the script name(in this case is main.py), so we take the second argument (index 1) as the book path
    # sys.argv is a list of command-line arguments passed on the terminal.
    book_path = sys.argv[1]
    
    # Get book contents
    book_content = get_book_content(book_path)

    # Get the number of words in the book
    num_words = get_num_words(book_content)

    # Get the character and its count in the book
    # For example: {"a": 100, "b": 50, ...}
    chars_dict = get_num_chars(book_content)

    # Format the dict of characters 
    # For example: [{"char": "a", "num": 100}, {"char": "b", "num": 50}, ...]
    # Also insert only the characters that are alphabetic and ignore the rest of the characters
    # Sort the list of characters based on the count in descending order
    sorted_characters = sort_chars_list(chars_dict)

    # Print the results
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
    
if __name__ == "__main__":
    main()