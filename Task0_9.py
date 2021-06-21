def find_vowel(word, vowels):
    #used to ignore case sensitity
    # using for to compare it with the string hat contains vowels
    word=word.casefold()
    check = [each for each in word if each in vowels]

    print("vowels: ", ','.join(set(check)))


word = 'Reorganized'
vowels = 'aeiou'

find_vowel(word, (vowels))
