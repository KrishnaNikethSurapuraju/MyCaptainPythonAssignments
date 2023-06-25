def frequent(string):

    letters_dict = {}

    for letter in string:
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1

    sorted_dict = sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)

    for item in sorted_dict:
        print(item[0], "=", item[1])


string = input("Please enter a string ")

frequent(string)
