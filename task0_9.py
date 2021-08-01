def find_vowel(word):
    word = word.casefold()
    vowels = "aeiou"
    check = [each for each in word if each in vowels]
    print("Vowels:", ", ".join(set(check)))


if __name__ == "__main__":
    find_vowel("Umuzi")
