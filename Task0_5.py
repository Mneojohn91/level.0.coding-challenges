def triangle_area(side1, side2, side3):
    semi_perimeter = (side1 + side2 + side3) / 2
    formula = (
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    ) ** (1 / 2)
    return int(formula)


def main():

    print(triangle_area(6, 5, 5))


if __name__ == "__main__":
    main()
