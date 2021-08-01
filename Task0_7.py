def convert_to_fahrenheit(degree_celsius):
    temperature = (degree_celsius * (9 / 5)) + 32
    return temperature

def convert_to_celsius(degree_fahr):
    tempature = (degree_fahr - 32) * 5 / 9
    return tempature


if __name__ == "__main__":
    print(convert_to_fahrenheit(15))
    print(convert_to_celsius(95))
