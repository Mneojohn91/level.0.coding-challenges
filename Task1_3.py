def test():


    num1 = 50
    num2 = 12
    sum_of = num2 + num1
    total_sum = 65
    print('total sum is: ', sum_of)
    if (num2 == total_sum or num1 == 65) or sum_of == total_sum:
        return True
    else:
        return False


print(test())
