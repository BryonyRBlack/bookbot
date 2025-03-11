from stats import word_count
from stats import get_book_text
from stats import count_character
from stats import sorted_dic
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    character_count = count_character(book_text)
    dictionary = sorted_dic(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in dictionary:
        char = char_dict["char"]
        count = char_dict["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()