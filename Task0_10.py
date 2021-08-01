def common_letter(word1, word2):
    word1 = word1.casefold()
    word2 = word2.casefold()
    common_word = ""
    for alphabet in word1:
        if alphabet in word2:
            common_word += alphabet
    print("Common letters: ", ", ".join(common_word), end=" ")


if __name__ == "__main__":
    common_letter("Eckard", "Berry")
