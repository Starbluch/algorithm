
input_chislo = input("Enter a string: ")
search_word = input("Enter the word to search for: ")
count = 0
input = 0
word = 0

# consecutive cycles
for char in input_chislo:
    input += 1

for char in search_word:
    word += 1

for i in range(input - word + 1):
    match = True
    for a in range(word):
        if input_chislo[i + a] != search_word[a]:
            match = False
            break
    if match:
        count += 1

print(search_word, count)
