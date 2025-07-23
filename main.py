from stats import count_characters

def get_book_text(books):
    with open(books) as f:
        return f.read()



def main():
    books = "books/frankenstein.txt"
    book_content = get_book_text(books)
    count_characters(book_content)
    

main()