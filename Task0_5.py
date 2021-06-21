a = 20
b = 20
c = 24
# s_p is the semi-perimeter
s_p = (a + b + c) / 2
area = (s_p * (s_p - a) * (s_p - b) * (s_p - c)) ** (1 / 2)

print("the area is: ", area)
