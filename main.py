import sys
from stats import get_num_words, get_num_chars, sort_chars_list

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents

def main():
    # Make sure there are two arguments given
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Take the relative path of file from the second argument
    book_path = sys.argv[1]
    
    # Get book contents
    book_text = get_book_text(book_path)

    # Count the total of words
    words_len = get_num_words(book_text)

    # find the character and its count (first step)
    chars_dict = get_num_chars(book_text)

    # change the dict format and sort it from greatest to least by a count
    sorted_characters = sort_chars_list(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_len} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
    
if __name__ == "__main__":
    main()