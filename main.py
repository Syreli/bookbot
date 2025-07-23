from stats import count_characters
from stats import get_word_count
from stats import sort_on
from stats import get_letter_list

def get_book_text(books):
    with open(books) as f:
        return f.read()



def main():
    books = "books/frankenstein.txt"
    book_content = get_book_text(books)
    get_word_count(book_content)
    character_dict = count_characters(book_content)
    letter_list = get_letter_list(character_dict)
    letter_list.sort(reverse=True, key=sort_on)
    

    print("=========== BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt..")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_content)} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    


main()