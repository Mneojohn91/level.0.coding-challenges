def highest_number(*number):
    list1 = list(number)
    highest = number[0]
    for i in list1:
        if i > highest:
            highest = i
    return highest

def main():

    print(highest_number(1, 22, 34, 7))
if __name__ == "__main__":
    main()
