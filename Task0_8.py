num = 230
def convert():
    minutes = (num-(60*(num//60)))
    hours =num//60
    if minutes> 1 and hours>1:
        print(hours, 'hours,', minutes, 'minutes')

    elif minutes ==1 and hours > 1:
        print(hours,'hours,', minutes, "minute")
    elif hours == 1 and minutes > 1:
        print(hours,'hour,', minutes, 'minutes')
    elif hours <= 1 and minutes >1:
        print(hours,'hour,', minutes, 'minutes')
    else:
        print(hours, 'hour, ' , minutes,'minute')

convert()
