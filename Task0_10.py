def common_letter(word1, word2):
    print("Common letters: ", ",".join(set(word1) & set(word2)))


def main():

    common_letter("satisfied", "recognised")
if __name__=="__main__":
    main()