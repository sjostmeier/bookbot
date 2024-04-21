def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_number = get_word_number(text)
    print(f"The book contains {word_number} number of words")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_number(text):
    words = text.split()
    return len(words)



main()
