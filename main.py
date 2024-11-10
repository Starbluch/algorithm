user_input = input("Enter a string: ")
search_char = input("Enter the character to search for: ")

count = 0

for char in user_input:
    if char == search_char:
        count += 1

print(search_char,count)