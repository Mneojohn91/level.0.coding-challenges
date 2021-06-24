


def common_letter(word1,word2):
    letter = ','.join(set(word1) & set(word2))
    print  (letter)




common_letter('recoup','regretted')
