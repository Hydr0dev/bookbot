from stats import get_word_count, get_char_count, sort_char_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
       return f.read()

def main():
    if len(sys.argv) == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char_dict = sort_char_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sorted_char_dict:
        char = c["char"]
        count = c["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()
