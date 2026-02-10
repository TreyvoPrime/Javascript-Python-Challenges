word = input("What is your word: ")
def vowels(word):
    vowels = "aeiou"

    number_vowels = 0
    for i in word:
        if i in vowels:
            number_vowels = number_vowels + 1
            print("number of vowels", number_vowels)
vowels(word)