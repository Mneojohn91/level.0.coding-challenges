


def common_letter(word1,word2):
    letter = ' , '.join(set(word1) & set(word2))
    print ("common letters: ", (letter))
word1 = ''
word2 = ""



common_letter('recoup','regretted')
