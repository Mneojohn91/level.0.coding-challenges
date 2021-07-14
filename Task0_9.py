def find_vowel(word):
    word = word.casefold()
    vowels = "aeiou"
    check = [each for each in word if each in vowels]
    print(",".join(set(check)))


find_vowel("rEcognizEd")
