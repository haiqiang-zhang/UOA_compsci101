def main():
    item_code = "ABC123"
    price = get_item_price(item_code)
    print(item_code, ": $", price, sep="")
    print("BED173: $", get_item_price("BED173"), sep="")
    print("FAB473: $", get_item_price("FAB473"), sep="")


def get_item_price(item_code):
    if item_code[0] == "A":
        return 100
    elif item_code[0] == "B":
        return 80
    else:
        return 50


main()