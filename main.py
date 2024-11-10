def numeric_letter():
    user_input = input("Enter a string: ")
    count_1 = 0
    count_2 = 0
    for char in user_input:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            count_1 += 1
        elif '0' <= char <= '9':
            count_2 += 1

    print("Number of letters:", count_1)
    print("Number of digits:", count_2)


numeric_letter()