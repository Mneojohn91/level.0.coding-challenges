def area_of(side1,side2,side3):


    formula = (s_p * (s_p - side1) * (s_p - side2) * (s_p - side3)) ** (1 / 2)
    print ( formula)

# s_p is the semi-perimeter
s_p = (20 + 20 + 24) / 2

print()
area_of(20,20,24)
