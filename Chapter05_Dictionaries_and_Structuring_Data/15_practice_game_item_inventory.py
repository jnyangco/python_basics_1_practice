inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def show_all_inventory(stuffs):
    for key, value in stuffs.items():
        print(f"{key} -> {value}")


def get_item_count_in_inventory(item, stuffs):
    return stuffs.get(item.lower())




show_all_inventory(inventory)

gold_coin_total = get_item_count_in_inventory("gold coin", inventory)
print(gold_coin_total)
