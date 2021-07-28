def common_letter(word1, word2):
    word1= word1.casefold()
    word2= word2.casefold()
    common_word =""
    for i in word1:
        if i in word2:
            common_word+=i
    print("Common letters: ",", ".join(common_word) ,end=" ")


def main():
    common_letter('Eckard', 'Berry')


if __name__ == "__main__":
    main()
