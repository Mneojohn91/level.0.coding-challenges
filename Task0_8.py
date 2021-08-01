def convert_to_time(number):
    minutes = number - (60 * (number // 60))
    hours = number // 60
    str_minutes = "minute"
    str_hours = "hour"
    if hours > 1 or hours == 0:
        str_hours = "hours"
    if minutes > 1 or minutes == 0:
        str_minutes = "minutes"

    number = f"{hours} {str_hours},{minutes} {str_minutes}"
    print(number)


if __name__ == "__main__":
    convert_to_time(120)
