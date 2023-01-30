# https://strefainzyniera.pl/artykul/996/struktury-danych

# kolejka
def queue():
    items = []
    max_len = 0
    curr_len = 0
    while True:
        item = int(input("Enter item: "))
        if item == -1:
            if len(items) > 0:
                items.pop(0)
                curr_len -= 1
        elif item == 0:
            print(max_len)
            break
        else:
            items.append(item)
            curr_len += 1
            max_len = max(max_len, curr_len)

        print(items)

queue()