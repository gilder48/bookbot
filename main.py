from stats import get_num_words, count_char, sort_dict
import sys

def get_book_text(path):
        with open(path) as f:
            file_contents = f.read()
            return file_contents
        
def print_report(word_count, char_count_list):
     print("============ BOOKBOT ============\n" \
     "Analyzing book found at books/frankenstein.txt...\n" \
     "----------- Word Count ----------\n" \
     f"Found {word_count} total words\n" \
     "--------- Character Count -------")
     for item in char_count_list:
          print(f"{item["char"]}: {item["num"]}")
     print("============= END ===============")


def main():
    args = sys.argv
    if len(args) != 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    text = get_book_text(args[1])
    num_words = get_num_words(text)
    char_dict = count_char(text)
    sort_list = sort_dict(char_dict)
    print_report(num_words, sort_list)

main()