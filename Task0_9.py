def find_vowel(word):
    #used to ignore case sensitity
    # using for to compare it with the string hat contains vowels
    word=word.casefold()
    vowels = 'aeiou'

    check = [each for each in word if each in vowels]

    print( ','.join(set(check)))



find_vowel('recognized')
