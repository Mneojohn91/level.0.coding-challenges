def tempature_Fahrenheit(degree_celsius):
    temperature = (degree_celsius * (9 / 5)) + 32
    print(temperature, "degrees fahrenheit")


tempature_Fahrenheit(12)


def tempature_celsius(degree_fahr):
    tempature = (degree_fahr - 32) * 5 / 9
    print(tempature, "degrees celsius")


tempature_celsius(95)

