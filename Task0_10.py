def common_letter(word1, word2):
    word1= word1.casefold()
    word2= word2.casefold()
    print("Common letters: ", ", ".join(set(word1) & set(word2)))


def main():
    common_letter('Eckard', 'Berry')


if __name__ == "__main__":
    main()
