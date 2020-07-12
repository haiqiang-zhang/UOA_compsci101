def get_change(items, price_per_item, amount_tendered):
    result = round(amount_tendered - (items*price_per_item),2)
    return result

print("$" + str(get_change(2, 2.225, 5.0)))
