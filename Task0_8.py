def convert_to_time(number):
    minutes = number - (60 * (number // 60))
    hours = number // 60
    if hours == 0 and minutes==0:
        print(hours, "hours,", minutes, "minutes")
    if hours == 1 and minutes==0:
	    print(hours, "hour,", minutes, "minutes")
    elif hours == 0 and minutes==1:
        print(hours,"hours", minutes,"minute")
    elif minutes > 1 and hours > 1:
        print(hours, "hours,", minutes, "minutes")
    elif minutes == 1 and hours > 1:
        print(hours, "hours,", minutes, "minute")
    elif hours == 1 and minutes > 1:
        print(hours, "hour,", minutes, "minutes")
    elif hours <= 1 and minutes > 1:
        print(hours, "hour,", minutes, "minutes")
    else:
        print(hours, "hour, ", minutes, "minute")


def main():

    convert_to_time(1)


if __name__ == "__main__":
    main()
