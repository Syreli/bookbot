def count_characters(book_content):
    letter_count = {}
    for letter in book_content.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return print(letter_count)
