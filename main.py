
def text():
    text = input("Enter the line: ")
    search_word = input("Enter a word to search for: ")
    replace_word = input("Enter a replacement word: ")
    result = text.replace(search_word, replace_word)
    print("Result:", result)


text()
