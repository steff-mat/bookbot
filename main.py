import sys
from stats import get_num_words, get_char_count, get_sorted_letters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_sorted_letters(sys.argv[1])

main()
