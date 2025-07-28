import sys
from stats import count_characters
from stats import get_word_count
from stats import sort_on
from stats import get_letter_list


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(books):
    with open(books) as f:
        return f.read()


def main():
    books = sys.argv[1]
    book_content = get_book_text(books)
    get_word_count(book_content)
    character_dict = count_characters(book_content)
    letter_list = get_letter_list(character_dict)
    letter_list.sort(reverse=True, key=sort_on)
    

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}..")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_content)} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    
main()