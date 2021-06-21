word1 = 'program'
word2 = 'recoup'


def common_letter(letter):
    print ("common letters: ", (letter))


letter = ' , '.join(set(word1) & set(word2))
common_letter(letter)
