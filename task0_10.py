def common_letter(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    same_letters = [each for each in word1 if each in word2]
    same_letters = ", ".join(set(same_letters))
    print("Common letters: ", same_letters)


if __name__ == "__main__":
    common_letter("EckardRe", "BeerryE")
