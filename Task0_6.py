def highest_number(*number):
    highest_numbers = list(number)
    highest_numbers.sort()
    print(highest_numbers[-1])


highest_number(1, 3, 2)