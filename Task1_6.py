def Longest_word(words):
    # sorting list by length
    words.sort(key=len)
    longest = len(words[-1])
    for i in words:
        if len(i) == len(words[-1]):  # compare words in lists with longest word

            print(i)


words = ["the", "quick", "chicken", 'program', "brown", "fox", "ate", "my"]

Longest_word(words)
