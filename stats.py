def get_word_count(book_content):
    words = book_content.split()
    return len(words)


def count_characters(book_content):
    letter_count = {}
    for letter in book_content.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def get_letter_list(letter_count):
    letter_list = []
    for key, value in letter_count.items():
        letter_sort = {"char": key, "num": value}
        letter_list.append(letter_sort)
    return letter_list

def sort_on(item):
    return item["num"]



        
    
    

    
