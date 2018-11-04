''' Project #4.1
The game "pig Latin"
'''
while True:
    phrase = input('Enter a phrase in Russian: ')
    letter = input('Enter one consonant letter: ')
    new_phrase = ''

    # Собираем новую строку.
    for char in range(0, len(phrase)):
        new_phrase += phrase[char]

        # Ищем гласные буквы.
        if phrase[char] == "а" or phrase[char] == "А" or \
            phrase[char] == "у" or phrase[char] == "У" or \
            phrase[char] == "е" or phrase[char] == "Е" or \
            phrase[char] == "ы" or phrase[char] == "Ы" or \
            phrase[char] == "ю" or phrase[char] == "Ю" or \
            phrase[char] == "о" or phrase[char] == "О" or \
            phrase[char] == "э" or phrase[char] == "Э" or \
            phrase[char] == "я" or phrase[char] == "Я" or \
            phrase[char] == "ё" or phrase[char] == "Ё" or \
            phrase[char] == "и" or phrase[char] == "И":
            new_phrase += (letter+phrase[char])

    char = 0
    correct_phrase= ''

    # Делаем заглавные буквы строчными, где это необходимо.
    while char < len(new_phrase):
        if new_phrase[char].isupper():
            correct_phrase += new_phrase[char]
            correct_phrase += new_phrase[char+1]
            correct_phrase += new_phrase[char+2].lower()
            char+=3
        else:
            correct_phrase += new_phrase[char]
            char +=1

    print(correct_phrase)