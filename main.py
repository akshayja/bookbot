import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    content = get_book_text(book_path) 
    
    print("----------- Word Count ----------")
    num_words = count_words(content)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    char_counts = count_characters(content)
    sorted_chars = sort_characters(char_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()